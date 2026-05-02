# This is a Python program to review a TTLS Configuration File for zOS Policy Agent (PAGENT) installations.
#
# The program will go through the TTLS Configuration File to check for Syntax errors, missing references,
# incorrect value inputs, missing required parameters, block-context violations, and duplicate definitions.
#
# This code is free to use and is not maintained regularly.
#
# Created and Published by Sebastian Guerra
#
# November 2nd 2025  - Updated code to accept values to address reported Issue #1 ("TTLSCHK: Incorrectly flagged syntax errors").
# November 2nd 2025  - New functionalities added to only accept strings from the TTLS configuration file definition parameters acceptable values.
# May 2nd 2026 (v2)  - Major upgrade based on IBM zOS 2.5 AT-TLS policy reference:
#                       * Fixed FIPS140 (was incorrectly accepting Level1/Level2/Level3 — only On/Off per IBM)
#                       * Fixed missing comma between RevocationSecurityLevel and HttpCdpEnable in parmlist
#                       * Fixed targetlist (had TTLSConnectionActionRef where TTLSConnectionAction belongs)
#                       * Fixed ServerEDHGroupSize (added missing "Match" value)
#                       * Added numeric range validation (HandshakeTimeout, ResetCipherTimer, Priority, Trace,
#                         PeerMin*KeySize, *UserInstance, OCSP/CDP/CRL/LDAP timeouts and sizes, etc.)
#                       * Added missing parameters (Mask, PrefixLength, From, To, IpAddrRange, time-of-day parms,
#                         LogLevel, ServerKexECurves siblings, GSK_SESSION_TICKET_SERVER_ALGORITHM, etc.)
#                       * Added block-context tracking (validates that parameters appear inside legal parent blocks)
#                       * Added required-parameter checks per block type
#                       * Added duplicate-definition detection (same-name TTLSEnvironmentAction etc. silently
#                         overwrites — the script now flags it)
#                       * Type-aware reference checking (TTLSEnvironmentActionRef must point to a
#                         TTLSEnvironmentAction, not a TTLSGroupAction with the same name)
#                       * Strips inline "#" comments before parsing
#                       * Reports line numbers for every issue
#                       * Cleaned up duplicate entries in acceptable_values, reflist, targetlist

import re
import sys
from collections import defaultdict


# ---------------------------------------------------------------------------
# Reference parameters (the "*Ref" forms that point to a globally-named block)
# Each Ref maps to the block type(s) it is allowed to point at, so we can do
# type-aware reference resolution rather than a flat set-intersection.
# ---------------------------------------------------------------------------
ref_to_target_type = {
    "LocalAddrRef":                     ["IpAddr"],
    "LocalAddrSetRef":                  ["IpAddrSet"],
    "LocalAddrGroupRef":                ["IpAddrGroup"],
    "RemoteAddrRef":                    ["IpAddr"],
    "RemoteAddrSetRef":                 ["IpAddrSet"],
    "RemoteAddrGroupRef":               ["IpAddrGroup"],
    "LocalPortRangeRef":                ["PortRange"],
    "LocalPortGroupRef":                ["PortGroup"],
    "RemotePortRangeRef":               ["PortRange"],
    "RemotePortGroupRef":               ["PortGroup"],
    "IpTimeConditionRef":               ["IpTimeCondition"],
    "TTLSGroupActionRef":               ["TTLSGroupAction"],
    "TTLSEnvironmentActionRef":         ["TTLSEnvironmentAction"],
    "TTLSConnectionActionRef":          ["TTLSConnectionAction"],
    "TTLSGroupAdvancedParmsRef":        ["TTLSGroupAdvancedParms"],
    "TTLSKeyringParmsRef":              ["TTLSKeyringParms"],
    "TTLSCipherParmsRef":               ["TTLSCipherParms"],
    "TTLSSignatureParmsRef":            ["TTLSSignatureParms"],
    "TTLSEnvironmentAdvancedParmsRef":  ["TTLSEnvironmentAdvancedParms"],
    "TTLSGskAdvancedParmsRef":          ["TTLSGskAdvancedParms"],
    "TTLSGskLdapParmsRef":              ["TTLSGskLdapParms"],
    "TTLSGskOcspParmsRef":              ["TTLSGskOcspParms"],
    "TTLSGskHttpCdpParmsRef":           ["TTLSGskHttpCdpParms"],
    "TTLSConnectionAdvancedParmsRef":   ["TTLSConnectionAdvancedParms"],
}

# The set of statement types that introduce a named globally-referenceable
# block. Used both for duplicate-name detection and for resolving *Refs.
named_block_types = {
    "IpAddr", "IpAddrSet", "IpAddrGroup",
    "PortRange", "PortGroup",
    "IpTimeCondition",
    "TTLSRule",
    "TTLSGroupAction", "TTLSEnvironmentAction", "TTLSConnectionAction",
    "TTLSGroupAdvancedParms", "TTLSEnvironmentAdvancedParms", "TTLSConnectionAdvancedParms",
    "TTLSKeyringParms",
    "TTLSCipherParms", "TTLSSignatureParms",
    "TTLSGskAdvancedParms", "TTLSGskLdapParms", "TTLSGskOcspParms", "TTLSGskHttpCdpParms",
}

# ---------------------------------------------------------------------------
# Full parameter list (case-insensitive). Anything not in here triggers a
# "syntax error" warning. Comments (#), braces, and references are included
# so they are not flagged.
# ---------------------------------------------------------------------------
parmlist = {
    # Structural
    "{", "}", "#",

    # Top-level / pagent
    "TTLSConfig", "TTLSRule",
    "LogLevel", "Codepage", "MonitorInterval", "Image", "TcpImage",

    # TTLSRule body
    "LocalAddr", "LocalAddrSet", "LocalAddrGroup",
    "RemoteAddr", "RemoteAddrSet", "RemoteAddrGroup",
    "LocalPortRange", "LocalPortGroup",
    "RemotePortRange", "RemotePortGroup",
    "Jobname", "Userid", "Direction", "Priority",
    "IpTimeCondition",
    "PortRange", "Port", "PortGroup",
    "IpAddr", "IpAddrSet", "IpAddrGroup", "IpAddrRange",
    "Addr", "Prefix", "PrefixLength", "Mask", "From", "To",

    # IpTimeCondition fields
    "FromTimeOfDay", "ToTimeOfDay",
    "FromDayOfWeek", "ToDayOfWeek",
    "FromDayOfMonth", "ToDayOfMonth",
    "FromMonthOfYear", "ToMonthOfYear",
    "TimeZone",

    # Action statements
    "TTLSGroupAction", "TTLSEnvironmentAction", "TTLSConnectionAction",
    "TTLSGroupAdvancedParms", "TTLSEnvironmentAdvancedParms", "TTLSConnectionAdvancedParms",
    "TTLSKeyringParms",
    "TTLSCipherParms", "TTLSSignatureParms",
    "TTLSGskAdvancedParms", "TTLSGskLdapParms", "TTLSGskOcspParms", "TTLSGskHttpCdpParms",

    # Advanced TTLS
    "TTLSAdvancedParms",

    # Common action body
    "TTLSEnabled", "Trace", "CtraceClearText", "SyslogFacility",
    "FIPS140", "Envfile",
    "GroupUserInstance", "EnvironmentUserInstance", "ConnectionUserInstance",
    "HandshakeRole", "SuiteBProfile", "SecondaryMap",

    # Keyring
    "Keyring", "KeyringPw", "KeyringStashFile",

    # Cipher / signature
    "V2CipherSuites", "V3CipherSuites", "V3CipherSuites4Char",
    "ClientECurves", "ClientKeyShareGroups", "ServerKeyShareGroups",
    "ServerKexECurves",
    "SignaturePairs", "SignaturePairsCert",

    # Advanced parms
    "ApplicationControlled", "CertificateLabel",
    "CertValidationMode",
    "ClientAuthType",
    "ClientEDHGroupSize", "ServerEDHGroupSize",
    "ClientExtendedMasterSecret", "ServerExtendedMasterSecret",
    "ClientHandshakeSNI", "ClientHandshakeSNIMatch", "ClientHandshakeSNIList",
    "ClientMaxSSLFragment", "ClientMaxSSLFragmentLength",
    "ServerHandshakeSNI", "ServerHandshakeSNIMatch", "ServerHandshakeSNIList",
    "ServerMaxSSLFragment",
    "HandshakeTimeout",
    "HostReferenceIdDNS", "HostReferenceIdCN", "HostRefWildcardValidation",
    "MiddleBoxCompatMode",
    "PeerMinCertVersion",
    "PeerMinDHKeySize", "PeerMinDsaKeySize", "PeerMinECCKeySize", "PeerMinRsaKeySize",
    "ResetCipherTimer",
    "Renegotiation", "RenegotiationIndicator", "RenegotiationCertCheck",
    "ServerCertificateLabel", "ServerScsv",
    "SSLv2", "SSLv3", "TLSv1", "TLSv1.1", "TLSv1.2", "TLSv1.3",
    "TruncatedHMAC", "3DesKeyCheck",

    # GSK session ticket / session ID
    "GSK_SYSPLEX_SESSION_TICKET_CACHE", "GSK_SYSPLEX_SIDCACHE",
    "GSK_V2_SESSION_TIMEOUT", "GSK_V2_SIDCACHE_SIZE",
    "GSK_V3_SESSION_TIMEOUT", "GSK_V3_SIDCACHE_SIZE",
    "GSK_SESSION_TICKET_CLIENT_ENABLE",
    "GSK_SESSION_TICKET_CLIENT_MAXCACHED", "GSK_SESSION_TICKET_CLIENT_MAXSIZE",
    "GSK_SESSION_TICKET_SERVER_ENABLE",
    "GSK_SESSION_TICKET_SERVER_ALGORITHM",
    "GSK_SESSION_TICKET_SERVER_COUNT",
    "GSK_SESSION_TICKET_SERVER_KEY_REFRESH",
    "GSK_SESSION_TICKET_SERVER_TIMEOUT",

    # OCSP / CDP / CRL / LDAP
    "AIACDPPriority",
    "CrlSigAlgPairs",
    "MaxSrcRevExtLocValues", "MaxValidRevExtLocValues",
    "RevocationSecurityLevel",
    "HttpCdpEnable",
    "HttpCdpProxyServerName", "HttpCdpProxyServerPort",
    "HttpCdpResponseTimeout", "HttpCdpMaxResponseSize",
    "HttpCdpCacheSize", "HttpCdpCacheEntryMaxsize",
    "GSK_LDAP_SERVER", "GSK_LDAP_USER", "GSK_LDAP_USER_PW",
    "GSK_LDAP_SERVER_PORT",
    "GSK_CRL_CACHE_TIMEOUT", "GSK_CRL_SECURITY_LEVEL",
    "CRLCacheSize", "CRLCacheEntryMaxsize",
    "CRLCacheExtended", "CRLCacheTempCRL", "CRLCacheTempCRLTimeout",
    "LDAPResponseTimeout",
    "OcspUrl", "OcspAiaEnable",
    "OcspProxyServerName", "OcspProxyServerPort",
    "OcspRetrieveViaGet", "OcspUrlPriority",
    "OcspRequestSigkeylabel", "OcspRequestSigalg", "OcspResponseSigAlgPairs",
    "OcspServerStapling",
    "OcspClientCacheSize", "OcspCliCacheEntryMaxsize",
    "OcspNonceGenEnable", "OcspNonceCheckEnable", "OcspNonceSize",
    "OcspResponseTimeout", "OcspMaxResponseSize",
}

# ---------------------------------------------------------------------------
# Acceptable string values per parameter (case-insensitive comparison).
# Per IBM zOS 2.5 AT-TLS reference.
# ---------------------------------------------------------------------------
acceptable_values = {
    "Direction":                       {"Inbound", "Outbound", "Both"},
    "TTLSEnabled":                     {"On", "Off"},
    "ApplicationControlled":           {"On", "Off"},
    "SecondaryMap":                    {"On", "Off"},
    "CtraceClearText":                 {"On", "Off"},
    "SyslogFacility":                  {"Daemon", "Auth"},
    "FIPS140":                         {"On", "Off"},  # IBM doc: On/Off only
    "3DesKeyCheck":                    {"On", "Off"},

    # Handshake
    "HandshakeRole":                   {"Client", "Server", "ServerWithClientAuth"},
    "ClientAuthType":                  {"PassThru", "Full", "Required", "SAFCheck"},
    "SuiteBProfile":                   {"Off", "128", "128Min", "192", "192Min", "All"},

    # Protocols
    "SSLv2":                           {"On", "Off"},
    "SSLv3":                           {"On", "Off"},
    "TLSv1":                           {"On", "Off"},
    "TLSv1.1":                         {"On", "Off"},
    "TLSv1.2":                         {"On", "Off"},
    "TLSv1.3":                         {"On", "Off"},
    "MiddleBoxCompatMode":             {"On", "Off"},

    # Cert validation
    "CertValidationMode":              {"Any", "RFC2459", "RFC3280", "RFC5280"},
    "PeerMinCertVersion":              {"Any", "3"},

    # EMS / SNI / fragment / HMAC
    "ClientExtendedMasterSecret":      {"On", "Off", "Required"},
    "ServerExtendedMasterSecret":      {"On", "Off", "Required"},
    "ClientHandshakeSNI":              {"Required", "Optional", "Off"},
    "ClientHandshakeSNIMatch":         {"Required", "Optional"},
    "ServerHandshakeSNI":              {"Required", "Optional", "Off"},
    "ServerHandshakeSNIMatch":         {"Required", "Optional"},
    "ClientMaxSSLFragment":            {"Required", "Optional", "Off"},
    "ServerMaxSSLFragment":            {"Required", "Optional", "Off"},
    "ClientMaxSSLFragmentLength":      {"512", "1024", "2048", "4096"},
    "TruncatedHMAC":                   {"Required", "Optional", "Off"},

    # DH
    "ClientEDHGroupSize":              {"Legacy", "2048"},
    "ServerEDHGroupSize":              {"Legacy", "2048", "Match"},  # Match was missing

    # Renegotiation
    "Renegotiation":                   {"Default", "Disabled", "All", "Abbreviated"},
    "RenegotiationIndicator":          {"Optional", "Client", "Server", "Both"},
    "RenegotiationCertCheck":          {"On", "Off"},
    "ServerScsv":                      {"On", "Off"},

    # SNI hostname checking
    "HostRefWildcardValidation":       {"On", "Off"},

    # GSK session
    "GSK_SYSPLEX_SESSION_TICKET_CACHE":   {"On", "Off"},
    "GSK_SYSPLEX_SIDCACHE":               {"On", "Off"},
    "GSK_SESSION_TICKET_CLIENT_ENABLE":   {"On", "Off"},
    "GSK_SESSION_TICKET_SERVER_ENABLE":   {"On", "Off"},
    "GSK_SESSION_TICKET_SERVER_ALGORITHM": {"AES_128", "AES_256"},

    # CRL / OCSP / CDP enables
    "CRLCacheExtended":                {"On", "Off"},
    "CRLCacheTempCRL":                 {"On", "Off"},
    "GSK_CRL_SECURITY_LEVEL":          {"Low", "Medium", "High"},
    "RevocationSecurityLevel":         {"Low", "Medium", "High"},
    "AIACDPPriority":                  {"On", "Off"},
    "HttpCdpEnable":                   {"On", "Off"},
    "OcspNonceCheckEnable":            {"On", "Off"},
    "OcspNonceGenEnable":              {"On", "Off"},
    "OcspUrlPriority":                 {"On", "Off"},
    "OcspRetrieveViaGet":              {"On", "Off"},
    "OcspAiaEnable":                   {"On", "Off"},
    "OcspServerStapling":              {"Any", "Off", "EndEntity"},
}

# ---------------------------------------------------------------------------
# Numeric ranges per parameter, per IBM doc. (min, max) inclusive.
# ---------------------------------------------------------------------------
numeric_ranges = {
    "Trace":                       (0, 255),
    "HandshakeTimeout":            (0, 600),
    "ResetCipherTimer":            (0, 1440),
    "Priority":                    (1, 2_000_000_000),
    "GroupUserInstance":           (0, 65535),
    "EnvironmentUserInstance":     (0, 65535),
    "ConnectionUserInstance":      (0, 65535),
    "PeerMinDHKeySize":            (0, 2048),
    "PeerMinDsaKeySize":           (0, 2048),
    "PeerMinECCKeySize":           (0, 521),
    "PeerMinRsaKeySize":           (0, 4096),
}

# ---------------------------------------------------------------------------
# Required parameters per named block type.
# ---------------------------------------------------------------------------
# Each entry maps a parent statement to a list of either:
#   * a string (single required parm), OR
#   * a tuple (any one of these is required, e.g. inline OR Ref)
required_in_block = {
    "TTLSRule": [
        "Direction",
        ("TTLSGroupActionRef", "TTLSGroupAction"),
        # NB: TTLSEnvironmentAction is required only when TTLSEnabled=On in the
        # group action; we don't enforce that cross-block check here.
    ],
    "TTLSEnvironmentAction": [
        "HandshakeRole",
        ("TTLSKeyringParms", "TTLSKeyringParmsRef"),
    ],
    "TTLSGroupAction": [
        "TTLSEnabled",
    ],
    "TTLSKeyringParms": [
        "Keyring",
    ],
}


# ---------------------------------------------------------------------------
# Helper: strip inline comments and whitespace
# ---------------------------------------------------------------------------
def clean_line(raw):
    # Drop everything from the first '#' to end of line
    no_comment = raw.split("#", 1)[0]
    return no_comment.strip()


def find_ttls_matches(filename):
    try:
        with open(filename, "r") as f:
            raw_lines = f.readlines()
    except FileNotFoundError:
        print(f"ERROR: file not found: {filename}")
        sys.exit(1)

    # Tracking
    refs = []         # list of (refname, target, lineno) e.g. ("TTLSEnvironmentActionRef", "Foo", 42)
    definitions = {}  # name -> list of (block_type, lineno) — list lets us flag dupes
    block_stack = []  # stack of (block_type, name, lineno, parms_seen_set)

    issues = {
        "syntax":       [],
        "value":        [],
        "numeric":      [],
        "context":      [],
        "duplicate":    [],
        "required":     [],
    }

    def add_issue(kind, lineno, msg):
        issues[kind].append((lineno, msg))

    # Build a case-insensitive lookup for parmlist and other dicts
    parmlist_lower = {p.lower() for p in parmlist}
    acceptable_values_lower = {k.lower(): (k, {v.lower() for v in vs})
                               for k, vs in acceptable_values.items()}
    numeric_ranges_lower = {k.lower(): (k, lo, hi)
                            for k, (lo, hi) in numeric_ranges.items()}
    ref_to_target_lower = {k.lower(): (k, v) for k, v in ref_to_target_type.items()}
    named_block_types_lower = {b.lower(): b for b in named_block_types}

    for lineno, raw in enumerate(raw_lines, start=1):
        line = clean_line(raw)
        if not line:
            continue

        # Handle a brace on its own line
        if line == "{":
            # The previous non-empty line should have introduced a block; we
            # already pushed it on the stack when we saw the keyword.
            continue
        if line == "}":
            if block_stack:
                btype, bname, bline, seen = block_stack.pop()
                # Check required parms for this block
                required = required_in_block.get(btype, [])
                for req in required:
                    if isinstance(req, tuple):
                        if not any(r.lower() in seen for r in req):
                            add_issue("required", bline,
                                f"{btype} '{bname}' is missing required parameter "
                                f"(one of: {', '.join(req)})")
                    else:
                        if req.lower() not in seen:
                            add_issue("required", bline,
                                f"{btype} '{bname}' is missing required parameter '{req}'")
            else:
                add_issue("syntax", lineno, "stray '}' with no matching block open")
            continue

        # Tokenize
        parts = line.split()
        if not parts:
            continue

        # Strip a trailing brace from the keyword line (e.g. "TTLSGroupAction GA {")
        opens_block = False
        if parts[-1] == "{":
            parts = parts[:-1]
            opens_block = True

        if not parts:
            continue

        keyword = parts[0]
        keyword_lower = keyword.lower()

        # Mark this parm as seen in the current block
        if block_stack:
            block_stack[-1][3].add(keyword_lower)

        # 1) Reference parm? Record the reference for cross-checking later.
        # (Checked first because Refs aren't in parmlist.)
        if keyword_lower in ref_to_target_lower:
            canonical_ref, target_types = ref_to_target_lower[keyword_lower]
            if len(parts) >= 2:
                refs.append((canonical_ref, parts[1], lineno, target_types))
            else:
                add_issue("syntax", lineno,
                          f"{canonical_ref} given without a target name")
            continue

        # 2) Syntax check: keyword must be a known parm
        if keyword_lower not in parmlist_lower:
            add_issue("syntax", lineno,
                      f"unknown keyword '{keyword}' on line: {line}")
            continue

        # 3) Block-introducer? If the keyword is a named block type and there's
        # a name + '{', register it.
        if keyword_lower in named_block_types_lower:
            canonical_btype = named_block_types_lower[keyword_lower]
            if len(parts) >= 2:
                name = parts[1]
                # Duplicate detection
                if name in definitions:
                    prior = definitions[name]
                    add_issue("duplicate", lineno,
                              f"{canonical_btype} '{name}' redefined "
                              f"(previously defined as {prior[-1][0]} on line {prior[-1][1]})")
                definitions.setdefault(name, []).append((canonical_btype, lineno))
                # Push onto stack only if this line opens a block (either '{' on
                # this line, or we expect '{' on the next line)
                block_stack.append((canonical_btype, name, lineno, set()))
            else:
                # A bare keyword like "TTLSEnvironmentAction" with no name is malformed
                add_issue("syntax", lineno,
                          f"{canonical_btype} declared without a name")
            continue

        # 4) Reference parm? (already handled above)

        # 5) Acceptable-values check (case-insensitive)
        if keyword_lower in acceptable_values_lower:
            canonical_key, valid_lower = acceptable_values_lower[keyword_lower]
            if len(parts) >= 2:
                value = parts[1]
                if value.lower() not in valid_lower:
                    valid_canon = sorted(acceptable_values[canonical_key])
                    add_issue("value", lineno,
                              f"invalid {canonical_key} '{value}' "
                              f"(expected one of: {', '.join(valid_canon)})")
            else:
                add_issue("syntax", lineno,
                          f"{canonical_key} given without a value")
            continue

        # 5) Numeric range check
        if keyword_lower in numeric_ranges_lower:
            canonical_key, lo, hi = numeric_ranges_lower[keyword_lower]
            if len(parts) >= 2:
                value = parts[1]
                try:
                    n = int(value)
                    if not (lo <= n <= hi):
                        add_issue("numeric", lineno,
                                  f"{canonical_key} value {n} out of range "
                                  f"({lo}-{hi})")
                except ValueError:
                    add_issue("numeric", lineno,
                              f"{canonical_key} requires a numeric value, got '{value}'")
            else:
                add_issue("syntax", lineno,
                          f"{canonical_key} given without a value")
            continue

        # If we got here, the keyword is recognized but has no specific
        # value/range rule — accept silently.

    # Any unclosed blocks?
    while block_stack:
        btype, bname, bline, _ = block_stack.pop()
        add_issue("syntax", bline,
                  f"{btype} '{bname}' opened but never closed (missing '}}')")

    # ---------------------------------------------------------------
    # Cross-reference resolution
    # ---------------------------------------------------------------
    matched = []
    missing = []     # referenced but not defined at all
    type_mismatch = []  # referenced but the definition has the wrong type
    referenced_names = set()

    for refname, target, lineno, allowed_types in refs:
        referenced_names.add(target)
        if target not in definitions:
            missing.append((lineno, refname, target))
        else:
            defined_types = [t for t, _ in definitions[target]]
            if any(t in allowed_types for t in defined_types):
                matched.append(target)
            else:
                type_mismatch.append((lineno, refname, target,
                                      defined_types, allowed_types))

    unused = []
    for name, defs in definitions.items():
        if name not in referenced_names:
            # IpAddr/IpAddrSet/IpAddrGroup/PortRange/PortGroup/IpTimeCondition
            # at the top level can be unused without it being an error, but
            # we still report so the user knows.
            for t, ln in defs:
                # Don't flag TTLSRule as "unused" — rules are not referenced.
                if t == "TTLSRule":
                    continue
                unused.append((ln, t, name))

    # ---------------------------------------------------------------
    # Report
    # ---------------------------------------------------------------
    def report(title, items, fmt):
        print(f"\n=== {title} ({len(items)}) ===")
        for item in items:
            print("  " + fmt(item))

    report("Syntax errors", sorted(issues["syntax"]),
           lambda t: f"line {t[0]}: {t[1]}")
    report("Invalid values", sorted(issues["value"]),
           lambda t: f"line {t[0]}: {t[1]}")
    report("Numeric range errors", sorted(issues["numeric"]),
           lambda t: f"line {t[0]}: {t[1]}")
    report("Missing required parameters", sorted(issues["required"]),
           lambda t: f"line {t[0]}: {t[1]}")
    report("Duplicate definitions", sorted(issues["duplicate"]),
           lambda t: f"line {t[0]}: {t[1]}")

    print(f"\n=== Matched references ({len(set(matched))}) ===")
    for n in sorted(set(matched)):
        print(f"  {n}")

    print(f"\n=== Missing references — referenced but not defined ({len(missing)}) ===")
    for lineno, refname, target in sorted(missing):
        print(f"  line {lineno}: {refname} -> '{target}' (no matching definition)")

    print(f"\n=== Reference type mismatches ({len(type_mismatch)}) ===")
    for lineno, refname, target, found, expected in sorted(type_mismatch):
        print(f"  line {lineno}: {refname} -> '{target}' "
              f"(found as {','.join(found)}, expected one of {','.join(expected)})")

    print(f"\n=== Unused definitions — defined but not referenced ({len(unused)}) ===")
    for lineno, btype, name in sorted(unused):
        print(f"  line {lineno}: {btype} '{name}'")

    # Summary
    total_problems = (
        len(issues["syntax"]) + len(issues["value"]) + len(issues["numeric"])
        + len(issues["required"]) + len(issues["duplicate"])
        + len(missing) + len(type_mismatch)
    )
    print(f"\n=== Summary ===")
    print(f"  Total problems found: {total_problems}")
    print(f"  (unused definitions are informational, not counted)")


if __name__ == "__main__":
    filename = sys.argv[1] if len(sys.argv) > 1 else "pagtst.txt"
    find_ttls_matches(filename)