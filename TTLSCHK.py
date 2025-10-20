# This is a Python program to review a TTLS Configuration File for zOS Policy Agent (PAGENT) installations.
#
# The program will go through the TTLS Configuration File to check for Syntax errors, missing references and incorrect value inputs for the most common parameters.
#
# This code is free to use and it is not maintained regularly.
#
# Created and Published by Sebastian Guerra
#

def find_ttls_matches(filename):
    with open(filename, 'r') as f:
        lines = f.readlines()

# Sets to be used to check for referenced values:
    refs = set()
    actions = set()

# List of Reference Parameters:
    reflist=["LocalAddrRef",
    "LocalAddrSetRef",
    "LocalAddrGroupRef",
    "RemoteAddrRef",
    "RemoteAddrSetRef",
    "RemoteAddrGroupRef",
    "LocalPortRangeRef",
    "LocalPortGroupRef",
    "RemotePortRangeRef",
    "RemotePortGroupRef",
    "IpTimeConditionRef",
    "TTLSGroupActionRef",
    "TTLSEnvironmentActionRef",
    "TTLSConnectionActionRef",
    "TTLSGroupAdvancedParmsRef",
    "TTLSKeyringParmsRef",
    "TTLSCipherParmsRef",
    "TTLSSignatureParmsRef",
    "TTLSEnvironmentAdvancedParmsRef",
    "TTLSGskAdvancedParmsRef",
    "TTLSCipherParmsRef",
    "TTLSSignatureParmsRef",
    "TTLSConnectionAdvancedParmsRef"]

# List of Referenceable Parameters:
    targetlist=["LocalAddr",
    "LocalAddrSet",
    "LocalAddrGroup",
    "RemoteAddr",
    "RemoteAddrSet",
    "RemoteAddrGroup",
    "LocalPortRange",
    "LocalPortGroup",
    "RemotePortRange",
    "RemotePortGroup",
    "IpTimeCondition",
    "TTLSGroupAction",
    "TTLSEnvironmentAction",
    "TTLSConnectionActionRef",
    "TTLSGroupAdvancedParms",
    "TTLSKeyringParms",
    "TTLSCipherParms",
    "TTLSSignatureParms",
    "TTLSEnvironmentAdvancedParms",
    "TTLSGskAdvancedParms",
    "TTLSCipherParms",
    "TTLSSignatureParms",
    "TTLSConnectionAdvancedParms"
    ]

# List of All Parameters:
    parmlist=[
    "{",
    "}",
    "#",
    "Jobname",
    "Userid",
    "Direction",
    "IpTimeCondition",
    "Priority",
    "Keyring",
    "KeyringPw",
    "KeyringStashFile",
    "TTLSCipherParms",
    "TTLSConnectionAction",
    "TTLSAdvancedParms",
    "TTLSEnvironmentAction",
    "TTLSEnvironmentAdvancedParms",
    "TTLSGroupAction",
    "TTLSGroupAdvancedParms",
    "TTLSKeyringParms",
    "TTLSRule",
    "TTLSSignatureParms",
    "ClientECurves",
    "ClientKeyShareGroups",
    "ServerKeyShareGroups",
    "SignaturePairs",
    "SignaturePairsCert",
    "SecondaryMap",
    "SyslogFacility",
    "Envfile",
    "TTLSEnabled",
    "CtraceClearText",
    "Trace",
    "TTLSGroupAdvancedParmsRef",
    "FIPS140",
    "GroupUserInstance",
    "3DesKeyCheck",
    "ApplicationControlled",
    "CertificateLabel",
    "CertValidationMode",
    "ClientAuthType",
    "ClientEDHGroupSize",
    "ClientExtendedMasterSecret",
    "ClientHandshakeSNI",
    "ClientHandshakeSNIMatch",
    "ClientHandshakeSNIList",
    "ClientMaxSSLFragment",
    "ClientMaxSSLFragmentLength",
    "HandshakeTimeout",
    "HostReferenceIdDNS",
    "HostReferenceIdCN",
    "MiddleBoxCompatMode",
    "HostRefWildcardValidation",
    "PeerMinCertVersion",
    "PeerMinDHKeySize",
    "PeerMinDsaKeySize",
    "PeerMinECCKeySize",
    "PeerMinRsaKeySize",
    "ResetCipherTimer",
    "Renegotiation",
    "RenegotiationIndicator",
    "RenegotiationCertCheck",
    "ServerCertificateLabel",
    "ServerExtendedMasterSecret",
    "ServerHandshakeSNI",
    "ServerHandshakeSNIMatch",
    "ServerHandshakeSNIList",
    "ServerMaxSSLFragment",
    "ServerEDHGroupSize",
    "ServerScsv",
    "SSLv2",
    "SSLv3",
    "TLSv1",
    "TLSv1.1",
    "TLSv1.2",
    "TLSv1.3",
    "TruncatedHMAC",
    "HandshakeRole",
    "SuiteBProfile",
    "EnvironmentUserInstance",
    "ConnectionUserInstance",
    "V2CipherSuites",
    "V3CipherSuites",
    "V3CipherSuites4Char",
    "LocalAddrRef",
    "LocalAddrSetRef",
    "LocalAddrGroupRef",
    "RemoteAddrRef",
    "RemoteAddrSetRef",
    "RemoteAddrGroupRef",
    "LocalPortRangeRef",
    "LocalPortGroupRef",
    "RemotePortRangeRef",
    "RemotePortGroupRef",
    "IpTimeConditionRef",
    "TTLSGroupActionRef",
    "TTLSEnvironmentActionRef",
    "TTLSConnectionActionRef",
    "TTLSKeyringParmsRef",
    "TTLSCipherParmsRef",
    "TTLSSignatureParmsRef",
    "TTLSEnvironmentAdvancedParmsRef",
    "TTLSGskAdvancedParmsRef",
    "TTLSConnectionAdvancedParmsRef",
    "PortRange",
    "Port",
    "LocalAddr",
    "RemoteAddr",
    "LocalPortRange",
    "RemotePortRange",
    "TTLSGskAdvancedParms",
    "TTLSConnectionAdvancedParms",
    "Addr",
    "IpAddrGroup",
    "Prefix",
    "GSK_SYSPLEX_SESSION_TICKET_CACHE",
    "GSK_SYSPLEX_SIDCACHE",
    "GSK_V2_SESSION_TIMEOUT",
    "GSK_V2_SIDCACHE_SIZE",
    "GSK_V3_SESSION_TIMEOUT",
    "GSK_V3_SIDCACHE_SIZE",
    "GSK_SESSION_TICKET_CLIENT_ENABLE",
    "GSK_SESSION_TICKET_CLIENT_MAXCACHED",
    "GSK_SESSION_TICKET_CLIENT_MAXSIZE",
    "GSK_SESSION_TICKET_SERVER_ENABLE",
    "GSK_SESSION_TICKET_SERVER_ALGORITHM",
    "GSK_SESSION_TICKET_SERVER_COUNT",
    "GSK_SESSION_TICKET_SERVER_KEY_REFRESH",
    "GSK_SESSION_TICKET_SERVER_TIMEOUT",
    ]

# List of Acceptable Values for each Common Parameter:
    acceptable_values = {
    "Direction": {"Inbound", "Outbound", "Both"},
    "SyslogFacility": {"daemon", "auth"},
    "SecondaryMap": {"On", "Off"},
    "TTLSEnabled": {"On", "Off"},
    "CtraceClearText": {"On", "Off"},
    "FIPS140": {"On", "Off"},
    "3DesKeyCheck": {"On", "Off"},
    "ClientAuthType": {"PassThru", "Full","Required","SAFCheck"},
    "ClientEDHGroupSize": {"Legacy", "2048"},
    "ClientExtendedMasterSecret": {"On", "Off","Required"},
    "HandshakeRole": {"Client", "Server","ServerWithClientAuth"},
    "SSLv2": {"On", "Off"},
    "SSLv3": {"On", "Off"},
    "TLSv1": {"On", "Off"},
    "TLSv1.1": {"On", "Off"},
    "TLSv1.2": {"On", "Off"},
    "TLSv1.3": {"On", "Off"}

}
    
# Extract all names and references from each line to be processed:
    for line in lines:
        line = line.strip()
        parts = line.split()
        if len(parts) < 2:
            continue  

        # Logic for the Extraction and Matching for values and parameters:
        key, value = parts[0], parts[1]
        key_lower = key.lower()
        value_lower = value.lower()

        # Case-insensitive validation against acceptable values
        for valid_key, valid_values in acceptable_values.items():
            if key_lower == valid_key.lower():  
                # Convert all acceptable values to lowercase for comparison
                valid_values_lower = {v.lower() for v in valid_values}
                if value_lower not in valid_values_lower:
                    print(f"\nERROR on line: {line}\nInvalid {valid_key} '{value}'")
                break  # Break to stop checking once the correct key is found

        # Syntax validation (case-insensitive)
        if all(not line.lower().startswith(parm.lower()) for parm in parmlist):
            print(f"\nSYNTAX ERRORS on line: {line}\n")

        # Value Extraction to compare with Reference List:
        if any(line.lower().startswith(ref.lower()) for ref in reflist):
            parts = line.split()
            if len(parts) >= 2:
                refs.add(parts[1])

        # Value Extraction to compare with Target List:
        if any(line.lower().startswith(target.lower()) for target in targetlist):
            parts = line.split()
            if len(parts) >= 2:
                actions.add(parts[1])

    # Actions to compare the sets:
    missing_actions = refs - actions
    unused_actions = actions - refs
    matched = refs & actions

    # Output for each Compare Action
    print("=== Matches ===")
    for name in sorted(matched):
        print(f"{name}")

    print("\n=== Missing Actions (referenced but not defined) ===")
    for name in sorted(missing_actions):
        print(f"{name}")

    print("\n=== Unused Actions (defined but not referenced) ===")
    for name in sorted(unused_actions):
        print(f"{name}")

# Filename Input
if __name__ == "__main__":
    filename = "pagtst.txt"  # Replace this field with your actual file name and path.
    find_ttls_matches(filename)
