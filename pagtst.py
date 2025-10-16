def find_ttls_matches(filename):
    with open(filename, 'r') as f:
        lines = f.readlines()

    refs = set()
    actions = set()

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
    "TTLSConnectionAdvancedParms"]
    
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
    "TTLSConnectionAdvancedParms"]
    
# Extract all names and references
    for line in lines:
        line = line.strip()
        if all(not line.startswith(parm) for parm in parmlist):
            print(f"\nSYNTAX ERRORS on line: {line}\n")
        if any(line.startswith(ref) for ref in reflist):
            parts = line.split()
            if len(parts) >= 2:
                refs.add(parts[1])
        if any(line.startswith(target) for target in targetlist):
            parts = line.split()
            if len(parts) >= 2:
                actions.add(parts[1])

    # Compare sets
    missing_actions = refs - actions
    unused_actions = actions - refs
    matched = refs & actions

    print("=== Matches ===")
    for name in sorted(matched):
        print(f"✓ {name}")

    print("\n=== Missing Actions (referenced but not defined) ===")
    for name in sorted(missing_actions):
        print(f"✗ {name}")

    print("\n=== Unused Actions (defined but not referenced) ===")
    for name in sorted(unused_actions):
        print(f"⚠ {name}")

# Example usage
if __name__ == "__main__":
    filename = "pagtst.txt"  # Replace with your actual file path
    find_ttls_matches(filename)