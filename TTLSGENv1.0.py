#!/usr/bin/env python3
"""
TTLSGEN.py - Interactive AT-TLS Rule Generator for z/OS Policy Agent (PAGENT)

Walks the user through a menu-driven Q&A and emits a complete, syntactically-correct
AT-TLS policy snippet (TTLSRule + TTLSGroupAction + TTLSEnvironmentAction +
TTLSConnectionAction + TTLSKeyringParms + TTLSCipherParms + TTLSEnvironmentAdvancedParms
+ TTLSConnectionAdvancedParms) ready to drop into a PAGENT config.

Companion to TTLSCHK_v2.py - whatever this generator emits should pass that checker
clean.

Created and Published by Sebastian Guerra
Initial version - May 2026
"""

import datetime
import sys


# ---------------------------------------------------------------------------
# Cipher-suite preset bundles. The mainframer rarely wants to type 8 cipher
# names by hand - they want "give me modern", "give me legacy compat", etc.
# Each preset is a list of (cipher_name, requires_TLSv12_or_higher_bool,
# is_TLSv13_only_bool). The 4-char hex codes in the comments come from the
# IBM "Cipher suite definitions" topic.
# ---------------------------------------------------------------------------
CIPHER_PRESETS = {
    "1": {
        "label": "Modern (TLS 1.3 only) - recommended for greenfield",
        "implies_protocols": {"SSLv2": "Off", "SSLv3": "Off", "TLSv1": "Off",
                              "TLSv1.1": "Off", "TLSv1.2": "Off", "TLSv1.3": "On"},
        "ciphers": [
            "TLS_AES_256_GCM_SHA384",        # 1302
            "TLS_AES_128_GCM_SHA256",        # 1301
            "TLS_CHACHA20_POLY1305_SHA256",  # 1303
        ],
    },
    "2": {
        "label": "Modern (TLS 1.3 + TLS 1.2 strong) - recommended for most servers",
        "implies_protocols": None,  # ask the user
        "ciphers": [
            # TLS 1.3
            "TLS_AES_256_GCM_SHA384",
            "TLS_AES_128_GCM_SHA256",
            "TLS_CHACHA20_POLY1305_SHA256",
            # TLS 1.2 - ECDHE+AEAD
            "TLS_ECDHE_ECDSA_WITH_AES_256_GCM_SHA384",
            "TLS_ECDHE_RSA_WITH_AES_256_GCM_SHA384",
            "TLS_ECDHE_ECDSA_WITH_AES_128_GCM_SHA256",
            "TLS_ECDHE_RSA_WITH_AES_128_GCM_SHA256",
        ],
    },
    "3": {
        "label": "Compatible (TLS 1.2 broad) - for older clients/partners",
        "implies_protocols": None,
        "ciphers": [
            "TLS_ECDHE_ECDSA_WITH_AES_256_GCM_SHA384",
            "TLS_ECDHE_RSA_WITH_AES_256_GCM_SHA384",
            "TLS_ECDHE_ECDSA_WITH_AES_128_GCM_SHA256",
            "TLS_ECDHE_RSA_WITH_AES_128_GCM_SHA256",
            "TLS_ECDHE_ECDSA_WITH_AES_256_CBC_SHA384",
            "TLS_ECDHE_RSA_WITH_AES_256_CBC_SHA384",
            "TLS_ECDHE_ECDSA_WITH_AES_128_CBC_SHA256",
            "TLS_ECDHE_RSA_WITH_AES_128_CBC_SHA256",
        ],
    },
    "4": {
        "label": "FIPS-friendly (TLS 1.2 only - FIPS 140-2 does not cover TLS 1.3)",
        "implies_protocols": {"SSLv2": "Off", "SSLv3": "Off", "TLSv1": "Off",
                              "TLSv1.1": "Off", "TLSv1.2": "On", "TLSv1.3": "Off"},
        "ciphers": [
            "TLS_ECDHE_ECDSA_WITH_AES_256_GCM_SHA384",
            "TLS_ECDHE_RSA_WITH_AES_256_GCM_SHA384",
            "TLS_ECDHE_ECDSA_WITH_AES_128_GCM_SHA256",
            "TLS_ECDHE_RSA_WITH_AES_128_GCM_SHA256",
        ],
    },
    "5": {
        "label": "Custom - I'll enter ciphers manually",
        "implies_protocols": None,
        "ciphers": [],
    },
}


# ---------------------------------------------------------------------------
# Small input helpers - all UI prompts go through these so behavior is uniform
# ---------------------------------------------------------------------------
def banner(text):
    bar = "=" * 70
    print(f"\n{bar}\n  {text}\n{bar}")


def section(text):
    print(f"\n--- {text} ---")


def ask(prompt, default=None, allow_empty=False):
    """Free-text prompt with optional default."""
    suffix = f" [{default}]" if default is not None else ""
    while True:
        answer = input(f"{prompt}{suffix}: ").strip()
        if not answer:
            if default is not None:
                return default
            if allow_empty:
                return ""
            print("  (a value is required)")
            continue
        return answer


def ask_choice(prompt, options, default=None):
    """
    options: list of (key, label) tuples. User picks by key.
    Returns the chosen key.
    """
    print(prompt)
    for key, label in options:
        marker = " *" if key == default else "  "
        print(f"  {marker}{key}) {label}")
    while True:
        raw = input("Choice" + (f" [{default}]" if default else "") + ": ").strip()
        if not raw and default is not None:
            return default
        for key, _ in options:
            if raw.lower() == key.lower():
                return key
        print("  (please pick a listed option)")


def ask_yes_no(prompt, default=True):
    d = "Y/n" if default else "y/N"
    while True:
        raw = input(f"{prompt} [{d}]: ").strip().lower()
        if not raw:
            return default
        if raw in ("y", "yes"):
            return True
        if raw in ("n", "no"):
            return False
        print("  (answer y or n)")


def ask_int(prompt, default=None, lo=None, hi=None):
    while True:
        raw = ask(prompt, default=str(default) if default is not None else None)
        try:
            n = int(raw)
        except ValueError:
            print(f"  (must be a whole number)")
            continue
        if lo is not None and n < lo:
            print(f"  (must be >= {lo})")
            continue
        if hi is not None and n > hi:
            print(f"  (must be <= {hi})")
            continue
        return n


def ask_name(prompt, default=None, max_len=32):
    """
    Names of TTLS objects must be 1-32 characters per IBM. We accept any
    printable non-whitespace string in that length range.
    """
    while True:
        v = ask(prompt, default=default)
        if " " in v or "\t" in v:
            print("  (no spaces in a name)")
            continue
        if not (1 <= len(v) <= max_len):
            print(f"  (length must be 1-{max_len})")
            continue
        return v


# ---------------------------------------------------------------------------
# Walk through each section of the rule
# ---------------------------------------------------------------------------
def gather_identity():
    section("Rule identity")
    rule_name = ask_name("Rule name (1-32 chars, no spaces)", default="MyAppRule")
    base = rule_name  # Used to derive sub-statement names
    return rule_name, base


def gather_traffic_selectors():
    section("Traffic selectors - which connections this rule applies to")
    direction = ask_choice(
        "Direction:",
        [("1", "Inbound  (we are the listening side)"),
         ("2", "Outbound (we initiate)"),
         ("3", "Both")],
        default="1",
    )
    direction = {"1": "Inbound", "2": "Outbound", "3": "Both"}[direction]

    local_addr = ask("Local IP address or 'All'", default="All")
    remote_addr = ask("Remote IP address or 'All'", default="All")

    if direction == "Inbound":
        local_ports = ask("Local port range (e.g. 2023 or 8080-8090)", default="443")
        remote_ports = ask("Remote port range (e.g. 1024-65535 or 'All')",
                           default="1024-65535")
    elif direction == "Outbound":
        local_ports = ask("Local port range (e.g. 1024-65535)", default="1024-65535")
        remote_ports = ask("Remote port range (e.g. 443)", default="443")
    else:
        local_ports = ask("Local port range", default="443")
        remote_ports = ask("Remote port range", default="1024-65535")

    jobname = ask("Jobname (wildcards OK, e.g. MYAPP*; '*' for any)", default="*")
    userid = ask("Userid (optional, blank to skip)", default="", allow_empty=True)
    priority = ask_int("Priority (1-2000000000, higher wins)", default=255,
                       lo=1, hi=2_000_000_000)

    return {
        "direction": direction,
        "local_addr": local_addr,
        "remote_addr": remote_addr,
        "local_ports": local_ports,
        "remote_ports": remote_ports,
        "jobname": jobname,
        "userid": userid,
        "priority": priority,
    }


def gather_handshake_role(direction):
    section("Handshake role and authentication")
    if direction == "Outbound":
        # Outbound = we are the client
        role_default = "1"
    else:
        role_default = "2"
    role_key = ask_choice(
        "Handshake role:",
        [("1", "Client                 - we initiate the handshake"),
         ("2", "Server                 - we accept handshakes, no client cert needed"),
         ("3", "ServerWithClientAuth   - we accept handshakes and require/verify a client cert")],
        default=role_default,
    )
    role = {"1": "Client", "2": "Server", "3": "ServerWithClientAuth"}[role_key]

    client_auth_type = None
    if role == "ServerWithClientAuth":
        ca_key = ask_choice(
            "Client authentication method (ClientAuthType):",
            [("1", "PassThru  - bypass cert validation entirely"),
             ("2", "Full      - validate cert if presented, else allow"),
             ("3", "Required  - require cert and validate (default)"),
             ("4", "SAFCheck  - require cert, validate, and require RACF/SAF user mapping")],
            default="3",
        )
        client_auth_type = {"1": "PassThru", "2": "Full",
                            "3": "Required", "4": "SAFCheck"}[ca_key]

    return role, client_auth_type


def gather_tls_protocols(preset):
    section("TLS protocol versions to enable")
    if preset["implies_protocols"] is not None:
        enabled = [k for k, v in preset["implies_protocols"].items() if v == "On"]
        print(f"  (preset is fixed - enabling only: {', '.join(enabled)})")
        return dict(preset["implies_protocols"])

    print("Pick protocols to enable. SSLv2/SSLv3/TLSv1.0/TLSv1.1 are all deprecated.")
    enable_tls13 = ask_yes_no("Enable TLS 1.3?", default=True)
    enable_tls12 = ask_yes_no("Enable TLS 1.2?", default=True)
    enable_tls11 = ask_yes_no("Enable TLS 1.1? (deprecated, only for legacy partners)",
                              default=False)
    enable_tls10 = ask_yes_no("Enable TLS 1.0? (deprecated, only for legacy partners)",
                              default=False)

    if not (enable_tls13 or enable_tls12 or enable_tls11 or enable_tls10):
        print("  WARNING: every TLS version disabled - re-enabling TLS 1.2 as a safety net")
        enable_tls12 = True

    return {
        "SSLv2":   "Off",
        "SSLv3":   "Off",
        "TLSv1":   "On" if enable_tls10 else "Off",
        "TLSv1.1": "On" if enable_tls11 else "Off",
        "TLSv1.2": "On" if enable_tls12 else "Off",
        "TLSv1.3": "On" if enable_tls13 else "Off",
    }


def gather_cipher_suites():
    section("Cipher suites")
    print("Pick a preset, or choose Custom to enter your own.\n")
    options = [(k, v["label"]) for k, v in CIPHER_PRESETS.items()]
    pick = ask_choice("Cipher preset:", options, default="2")
    preset = dict(CIPHER_PRESETS[pick])  # shallow copy so we can mutate

    if pick == "5":
        print("Enter cipher suite names one per line. Blank line to finish.")
        print("Example names: TLS_AES_256_GCM_SHA384, "
              "TLS_ECDHE_ECDSA_WITH_AES_256_GCM_SHA384")
        custom = []
        while True:
            v = input("  cipher: ").strip()
            if not v:
                break
            custom.append(v)
        if not custom:
            print("  (no ciphers entered - falling back to preset 2)")
            preset = dict(CIPHER_PRESETS["2"])
        else:
            preset["ciphers"] = custom

    return preset


def gather_keyring_and_cert(role):
    section("Keyring and certificate")
    keyring = ask("Keyring name (e.g. USERID/RINGNAME or just RINGNAME)",
                  default="MYUSER/MYRING")

    cert_label = None
    server_cert_labels = []
    if role in ("Server", "ServerWithClientAuth"):
        print("Server-side: you may specify one or more ServerCertificateLabel values.")
        print("First one entered becomes the preferred cert; blank to skip and use the")
        print("keyring default certificate.")
        while True:
            label = input(f"  ServerCertificateLabel #{len(server_cert_labels)+1} "
                          f"(blank to finish): ").strip()
            if not label:
                break
            server_cert_labels.append(label)
            if len(server_cert_labels) >= 8:
                print("  (8 is the max)")
                break
    else:
        # Client side
        cert_label = ask("CertificateLabel for client auth (blank to use keyring default)",
                         default="", allow_empty=True)
        if cert_label == "":
            cert_label = None

    return keyring, cert_label, server_cert_labels


def gather_advanced(role, protocols):
    section("Advanced settings (press Enter to accept defaults)")
    application_controlled = ask_yes_no(
        "ApplicationControlled? (On = app explicitly starts TLS via SIOCTTLSCTL ioctl)",
        default=False,
    )
    handshake_timeout = ask_int("HandshakeTimeout in seconds (0-600)",
                                default=10, lo=0, hi=600)
    secondary_map = ask_yes_no("SecondaryMap? (typical for FTP control->data)",
                               default=False)

    fips140 = ask_yes_no("FIPS140 mode? (requires ICSF active)", default=False)
    if fips140 and protocols.get("TLSv1.3") == "On":
        print("  WARNING: FIPS 140-2 does not cover TLS 1.3. Disabling TLS 1.3.")
        protocols["TLSv1.3"] = "Off"
        if protocols.get("TLSv1.2") != "On":
            print("  Enabling TLS 1.2 since FIPS needs at least one supported protocol.")
            protocols["TLSv1.2"] = "On"

    return {
        "application_controlled": "On" if application_controlled else "Off",
        "handshake_timeout": handshake_timeout,
        "secondary_map": "On" if secondary_map else "Off",
        "fips140": "On" if fips140 else "Off",
    }


def gather_trace():
    section("Tracing")
    print("Trace levels (additive bitmask 0-255):")
    print("    0  = no tracing")
    print("    1  = errors to TCP/IP joblog")
    print("    2  = errors to syslogd")
    print("    4  = info (rule mapping, secure connection events) to syslogd")
    print("    8  = major events (debug) to syslogd")
    print("   16  = system SSL flow (debug) to syslogd")
    print("   32  = encrypted negotiation/headers (debug) to syslogd")
    print("  255  = all tracing")
    return ask_int("Trace level", default=2, lo=0, hi=255)


# ---------------------------------------------------------------------------
# Render the policy text
# ---------------------------------------------------------------------------
def render(rule, base, traffic, role, client_auth_type, protocols, preset,
           keyring, cert_label, server_cert_labels, advanced, trace):

    # Names for sub-statements, derived from the rule name
    ga_name  = f"{base}_GA"   # TTLSGroupAction
    ea_name  = f"{base}_EA"   # TTLSEnvironmentAction
    ca_name  = f"{base}_CA"   # TTLSConnectionAction
    kr_name  = f"{base}_KR"   # TTLSKeyringParms
    cp_name  = f"{base}_CP"   # TTLSCipherParms
    eap_name = f"{base}_EAP"  # TTLSEnvironmentAdvancedParms
    cap_name = f"{base}_CAP"  # TTLSConnectionAdvancedParms

    L = []
    stamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
    L.append(f"# AT-TLS policy generated {stamp} by TTLSGEN.py")
    L.append(f"# Rule: {rule}")
    L.append("# ----------------------------------------------------------------")
    L.append("")

    # ---- TTLSRule ----
    L.append(f"TTLSRule {rule}")
    L.append("{")
    L.append(f"  LocalAddr               {traffic['local_addr']}")
    L.append(f"  RemoteAddr              {traffic['remote_addr']}")
    L.append(f"  LocalPortRange          {traffic['local_ports']}")
    L.append(f"  RemotePortRange         {traffic['remote_ports']}")
    if traffic["jobname"] and traffic["jobname"] != "*":
        L.append(f"  Jobname                 {traffic['jobname']}")
    if traffic["userid"]:
        L.append(f"  Userid                  {traffic['userid']}")
    L.append(f"  Direction               {traffic['direction']}")
    L.append(f"  Priority                {traffic['priority']}")
    L.append(f"  TTLSGroupActionRef      {ga_name}")
    L.append(f"  TTLSEnvironmentActionRef {ea_name}")
    L.append(f"  TTLSConnectionActionRef {ca_name}")
    L.append("}")
    L.append("")

    # ---- TTLSGroupAction ----
    L.append(f"TTLSGroupAction {ga_name}")
    L.append("{")
    L.append("  TTLSEnabled             On")
    L.append(f"  Trace                   {trace}")
    if advanced["fips140"] == "On":
        L.append(f"  FIPS140                 On")
    L.append("}")
    L.append("")

    # ---- TTLSEnvironmentAction ----
    L.append(f"TTLSEnvironmentAction {ea_name}")
    L.append("{")
    L.append(f"  HandshakeRole           {role}")
    L.append(f"  TTLSKeyringParmsRef     {kr_name}")
    L.append(f"  TTLSCipherParmsRef      {cp_name}")
    L.append(f"  TTLSEnvironmentAdvancedParmsRef {eap_name}")
    L.append("}")
    L.append("")

    # ---- TTLSConnectionAction ----
    L.append(f"TTLSConnectionAction {ca_name}")
    L.append("{")
    L.append(f"  HandshakeRole           {role}")
    L.append(f"  TTLSCipherParmsRef      {cp_name}")
    L.append(f"  TTLSConnectionAdvancedParmsRef {cap_name}")
    L.append("}")
    L.append("")

    # ---- TTLSKeyringParms ----
    L.append(f"TTLSKeyringParms {kr_name}")
    L.append("{")
    L.append(f"  Keyring                 {keyring}")
    L.append("}")
    L.append("")

    # ---- TTLSCipherParms ----
    L.append(f"TTLSCipherParms {cp_name}")
    L.append("{")
    L.append(f"  # Preset: {preset['label']}")
    for c in preset["ciphers"]:
        L.append(f"  V3CipherSuites          {c}")
    L.append("}")
    L.append("")

    # ---- TTLSEnvironmentAdvancedParms ----
    L.append(f"TTLSEnvironmentAdvancedParms {eap_name}")
    L.append("{")
    L.append(f"  SSLv2                   {protocols['SSLv2']}")
    L.append(f"  SSLv3                   {protocols['SSLv3']}")
    L.append(f"  TLSv1                   {protocols['TLSv1']}")
    L.append(f"  TLSv1.1                 {protocols['TLSv1.1']}")
    L.append(f"  TLSv1.2                 {protocols['TLSv1.2']}")
    L.append(f"  TLSv1.3                 {protocols['TLSv1.3']}")
    L.append(f"  ApplicationControlled   {advanced['application_controlled']}")
    L.append(f"  HandshakeTimeout        {advanced['handshake_timeout']}")
    if client_auth_type:
        L.append(f"  ClientAuthType          {client_auth_type}")
    if role in ("Server", "ServerWithClientAuth"):
        for lbl in server_cert_labels:
            L.append(f"  ServerCertificateLabel  {lbl}")
    elif cert_label:
        L.append(f"  CertificateLabel        {cert_label}")
    L.append("}")
    L.append("")

    # ---- TTLSConnectionAdvancedParms ----
    L.append(f"TTLSConnectionAdvancedParms {cap_name}")
    L.append("{")
    L.append(f"  ApplicationControlled   {advanced['application_controlled']}")
    L.append(f"  SecondaryMap            {advanced['secondary_map']}")
    if role in ("Server", "ServerWithClientAuth"):
        for lbl in server_cert_labels:
            L.append(f"  ServerCertificateLabel  {lbl}")
    elif cert_label:
        L.append(f"  CertificateLabel        {cert_label}")
    L.append("}")

    return "\n".join(L) + "\n"


# ---------------------------------------------------------------------------
# Main flow
# ---------------------------------------------------------------------------
def main():
    banner("AT-TLS rule generator for z/OS PAGENT")
    print("This wizard will ask a series of questions and emit a complete AT-TLS")
    print("policy snippet. Press Ctrl-C at any time to abort.\n")
    print("Tip: the output is meant to be checked with TTLSCHK_v2.py before deploying.")

    rule_name, base = gather_identity()
    traffic = gather_traffic_selectors()
    role, client_auth_type = gather_handshake_role(traffic["direction"])
    preset = gather_cipher_suites()
    protocols = gather_tls_protocols(preset)
    keyring, cert_label, server_cert_labels = gather_keyring_and_cert(role)
    advanced = gather_advanced(role, protocols)
    trace = gather_trace()

    output = render(rule_name, base, traffic, role, client_auth_type,
                    protocols, preset, keyring, cert_label,
                    server_cert_labels, advanced, trace)

    banner("Generated policy")
    print(output)

    section("Save")
    if ask_yes_no("Save to a file?", default=True):
        default_path = f"{rule_name}.policy"
        path = ask("Output filename", default=default_path)
        try:
            with open(path, "w") as f:
                f.write(output)
            print(f"Wrote {path}")
        except OSError as e:
            print(f"Could not write: {e}")
    else:
        print("(not saved)")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\nAborted.")
        sys.exit(130)