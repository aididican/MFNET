# MFNET UTILS

## Purpose of this document

This document is meant to be a reference guide for zOS practicioners. Oriented mostly to Communications Server configuration, troubleshooting and related applications.

-----------------------------------------

# INDEX

## Communication Server Commands

[TPX](#tpx)


## Useful Commands (NOT Communications Server)

[Useful](#useful)

## File Transfer

[XMIT](#xmit)

[ConnectDirect](#connect)

[WinSCP](#winscp)

[FTP](#ftp)

[SSH Suite](#ssh)


## RACF

[Common](#common)

[Certificates](#certificates)

## ACF2

[Common](#usual)

[Certificates](#acf2cert)


## JCL

[REUSABLE JCL](#reusable)

[Parameters](#parameters)

[FileAid](#fileaid)

[SDSF](#sdsf)

[BPXBATCH](#bpxbatch)

[REXX](#rexx)

[VSAM](#vsam)

[SMPE](#smpe)

[EXAMPLES](#examples)















------------------------------
------------------------------
------------------------------


# Communication Server Commands

## TPX

https://techdocs.broadcom.com/us/en/ca-mainframe-software/traditional-management/ca-tpx-session-management/5-4/programming/tpx-programming/tpx-special-features-and-customization-tasks/customize-the-aptpx-member.html

```
Description of Statements
The following list explains the types of statements that are shown in the previous example.

	*TPX,PRINT=
	Tells the software whether to list the APTPX member in printouts of your log. Any log you send to 
	Broadcom
	 for diagnostic purposes should include a copy of this member. The default value is TPX,PRINT=ON. If you specify PRINT=OFF, you will not get a copy of this member in your log.

	*TPX,PRIMARY
	Defines the network name of your system and identifies this system as a PLU that all physical terminals communicate with. The name that initially appears in column one of this statement is TPX. You use this name when you specify your LOGON APPLID commands in VTAM. For example, if the name you specify here is TPX, you would issue LOGON APPLID(TPX).

	*TPX,SHARE
	Identifies a virtual terminal that is used with applications that allow users to share a single virtual terminal. You can define only one shared virtual terminal.

	*TPX,GROUP
	Identifies virtual terminals that can be used with applications that allow a group of users to share a virtual terminal, providing each user is accessing a different application through the virtual terminal.

	*TPX,UNIQUE
	Identifies virtual terminals that can be used with applications that require each user to have a separate virtual terminal.

	*TPX,APPLPPS
	Identifies virtual printers used for Application Passthrough Printer Support. For more information about Application Passthrough Printer Support, see the Administrating section.

	*TPX,USERPPS
	Identifies virtual printers that are used for User Passthrough Printer Support. For more information about User Passthrough Printer Support, see the Administrating section.
```

From <https://techdocs.broadcom.com/us/en/ca-mainframe-software/traditional-management/ca-tpx-session-management/5-4/programming/tpx-programming/tpx-special-features-and-customization-tasks/customize-the-aptpx-member.html> 

TPX Command Summary:   

```                                                 
      /sessid                      - Switch/activate named session      
      /A <ALL>                     - Activate implied or all sessions   
      /B                           - Access the TPX Mailbox system      
      /D sessid                    - Delete dynamically added session   
      /E CMD=/CHR=/etc             - Temporary change to user profile   
      /F                           - Return to LOGO                     
      /G <all>                     - Activate sessions without ACL      
      /H                           - Help                               
      /I <all>                     - Inactivate implied or all sessions 
      /J                           - Jump to next active session        
      /K                           - Logoff from TPX                    
      /L                           - Lock terminal                      
      /N sessid                    - Start session in PASS mode         
      /P sessid dest cls           - Capture session's screen image     
      /Q sessid dest               - Send screen from sessid to userid  
      /R                           - Reshow the last screen             
      /S sessid aclpgm             - Start an ACL prgm for sessid       
      /V sessid                    - Interrupt an ACL prgm for sessid   
      /W                           - Display TPX selection menu         

```

TPX Activate Session:

https://techdocs.broadcom.com/us/en/ca-mainframe-software/traditional-management/ca-tpx-session-management/5-4/administrating/general-administration/specifying-application-characteristics/add-or-modify-application-characteristics.html
TPXOPER
ACT applid

Virtual Terminal:

https://knowledge.broadcom.com/external/article/51044/tpxoper-display-for-dynamically-added-vt.html

https://knowledge.broadcom.com/external/article/19727/in-output-of-tpxoper-d-t-why-does-a-real.html

https://techdocs.broadcom.com/us/en/ca-mainframe-software/traditional-management/ca-tpx-session-management/5-4/operating/operator-commands/activate-command.html

https://techdocs.broadcom.com/us/en/ca-mainframe-software/traditional-management/ca-tpx-session-management/5-4/operating/operator-commands/display-command-for-virtual-terminals.html

```
D VT,ALL
D VT,INACT
D VT,ACT
```

https://techdocs.broadcom.com/us/en/ca-mainframe-software/traditional-management/ca-tpx-session-management/5-4/operating/operator-commands/modify-command.html

```
MOD VT=x,AVAIL
MOD VT=x,UNAVAIL
```

-----------------------------------------------------------------------------------------------------------------------------

# FILE TRANSFERS

## XMIT

SYNTAX

```
xmit user.node dsn('hlq.ql') outdsn('hlq.ql')
receive indsn('hlq.ql')
```

----------------------------------

## Connect Direct

Manuals

https://www.ibm.com/docs/en/scfz/5.2.0?topic=zos-signon-command

https://www.ibm.com/docs/en/scfz/5.2.0?topic=command-using-signon-through-batch-interface

https://www.ibm.com/docs/en/scfz/5.2.0?topic=sessions-signing-sterling-connectdirect-zos

https://www.ibm.com/docs/en/scfz/5.2.0?topic=zos-using-signon-through-iui

https://www.ibm.com/docs/en/scfz/5.2.0?topic=iui-setting-up-signon-defaults

https://www.ibm.com/docs/en/scfz/5.2.0?topic=iui-viewing-your-current-signon-parameters

https://www.ibm.com/docs/en/connect-direct/6.1.0?topic=errors-signon-iuiapi

https://www.ibm.com/docs/en/connect-direct/6.1.0?topic=administrative-connectdirect-secure-plus-commands

https://www.ibm.com/docs/en/connect-direct/6.1.0?topic=options-adding-remote-node-record-external-authentication-server

https://www.ibm.com/docs/en/connect-direct/6.1.0?topic=administrative-connectdirect-secure-plus-commands

https://www.ibm.com/docs/en/connect-direct/6.1.0?topic=zos-enable-validate-connectdirect-secure-plus-operation

https://www.ibm.com/docs/en/connect-direct/6.1.0?topic=zos-troubleshooting

-------------------------------------------------

## WinSCP

winscp.exe /console

open hostname
put C:/sadsad/asdad.txt HLQ.DATASET    // NO QUOTES

open -passive=off ftpes://${useridpass}:$cpassword@$hostname/
call site file=jes
ascii  //  binary
put ftpjcl.txt
exit

open ftpes - FTPS
open ftp - FTP
open - SFTP
open sftp - SFTP

With FTP you can use -passive=on or off

--------------------------------------------

## FTP

FTP USEFUL

Commands:

put
get
mput  - Copies all members from a PDS to another, it should be created
mget
mvsput - Allocates file with same attributes and copies all members
mvsget


1	AMBIGUOUS	false
2	?	false
3	ACCT	true
4	APPEND	true
5	ASCII	true
6	BINARY	true
7	CD	true
8	CLOSE	true
9	TSO	false
10	OPEN	true
11	DEBUG	false
12	DELIMIT	false
13	DELETE	true
14	DIR	true
15	EBCDIC	true
16	GET	true
17	HELP	false
18	LOCSTAT	true
19	USER	true
20	LS	true
21	MDELETE	true
22	MGET	true
23	MODE	true
24	MPUT	true
25	NOOP	true
26	PASS	true
27	PUT	true
28	PWD	true
29	QUIT	true
30	QUOTE	true
31	RENAME	true
32	SENDPORT	true
33	SENDSITE	false
34	SITE	false
35	STATUS	true
36	STRUCTURE	true
37	SUNIQUE	true
38	SYSTEM	true
40	TYPE	true
41	LCD	true
42	LOCSITE	true (see previous note in FTP subcommand codes)
43	LPWD	false
44	MKDIR	true
45	LMKDIR	true
46	EUCKANJI	true
47	IBMKANJI	true
48	JIS78KJ	true
49	JIS83KJ	true
50	SJISKANJI	true
51	CDUP	true
52	RMDIR	true
53	HANGEUL	true
54	KSC5601	true
55	TCHINESE	true
56	RESTART	false
57	BIG5	true
58	BLOCK	true
59	COMPRESS	true
60	FILE	true
61	PROXY	true
62	RECORD	true
63	SCHINESE	true
64	STREAM	true
65	GLOB	false
66	PROMPT	false
67	UCS2	true
68	!	true
70	DUMP	false
71	VERBOSE	false
72	CLEAR	true
73	CPROTECT	true
74	PRIVATE	true
75	PROTECT	true
76	SAFE	false
77	CCC	true
78	LANGUAGE	true
79	FEATURE	true
80	SRESTART	true
81	AUTH	true
82	mkfifo	true
83	MVSGET	true
84	MVSPUT	true

EXAMPLE:
                                 
lcd 'SYS3.R31'                   
type i                                    
locsite fwf                               
locsite lrecl=1024 recfm=fb blksize=6144  
locsite track pri=350 sec=100 vol=INST04  
mget *.F1 (repl                           
mget *.F2 (repl                           
mget *.SMPMCS (repl                       
mget *.JCL (repl                          
type a                                    
locsite lrecl=80   recfm=fb blksize=3120  
locsite track pri=2  sec=1 vol=INST04     
mget *.TXT (repl                          
quit    

SITE        -FTP default
QUOTE SITE  -Windows
LOCSITE     -zOS
CALL SITE   -WinSCP

https://www.ibm.com/support/pages/sitelocsite-commands-mvs-ftp

TSO Syntax:

```
Ftp hostname -d -v -f "//'FTPDATA.DSN(member)'"
```


FTPDATA Search Order

https://www.ibm.com/docs/en/zos/2.2.0?topic=protocol-ftp-configuration-statements-in-ftpdata

TSO shell
-f
SYSFTPD DD statement
tso_prefix.FTP.DATA
userid.FTP.DATA
/etc/ftp.data
SYS1.TCPPARMS(FTPDATA) data set
tcpip_hlq.FTP.DATA file

UNIX System Services shell
-f
$HOME/ftp.data
userid.FTP.DATA
/etc/ftp.data
SYS1.TCPPARMS(FTPDATA) data set
tcpip_hlq.FTP.DATA file

FTP TLS:

A z/OS® FTP client can use a virtual CERTAUTH key ring to authenticate the FTP server by following these steps:
The user specifies the following KEYRING directive in her FTP.DATA file:
KEYRING *AUTH*/*

The user directs FTP to use TLS by specifying -a TLS or -r TLS on the FTP command:
ftp –r TLS ftp.ibm.com
-d -v -f 

For PDS:
cd NEXTLQ: Like if the PDS is USERID.PDS(*)
You do:
open hostname (working directory "HLQ.")
cd PDS
mput or mget

For Binary Files:
https://www.ibm.com/support/pages/transfer-ptf-binary-bin-file-your-pc-mvs-system
Define the file attributes as: FB, LRECL 1024, BLKSIZE 27648
Use mput for the file transfer.

Continuation:

mvsget 'SYS3.SYNCLINK' +
'SYS3.SYNCLINK'
https://www.ibm.com/docs/en/zos/2.3.0?topic=ftp-examples-get-mget-mvsget-subcommands


FTP Client
https://www.ibm.com/docs/en/zos/2.4.0?topic=ftpdata-summary-ftp-client-server-configuration-statements

Subcommands to the server
https://www.ibm.com/docs/en/zos/2.3.0?topic=codes-ftp-subcommand
batch

https://www.ibm.com/docs/en/zos/2.4.0?topic=ftp-submitting-requests-in-batch


https://www.ibm.com/docs/en/zos/2.1.0?topic=ftp-ddname-support

https://www.ibm.com/docs/en/zos/2.2.0?topic=protocol-keyring-ftp-client-server-statement

Parameters

https://www.ibm.com/docs/en/zos/2.2.0?topic=ftp-command-entering-environment

https://www.ibm.com/docs/en/zos/2.1.0?topic=ftp-preparing-environment

https://community.bmc.com/s/article/How-can-I-use-variable-names-for-my-FTP-dataset-names

https://www.ibm.com/docs/en/zos/2.2.0?topic=applications-environment-variables

NETRC

https://www.ibm.com/docs/en/zos/2.3.0?topic=ftp-netrc-data-set

https://www.ibm.com/docs/en/zos/2.1.0?topic=host-using-netrc-data-set

ENVAR

https://www.ibm.com/support/pages/specifying-tcpip-server-parameters-jcl

SYSFTPD DD statement
DSN=dsnname,DISP=SHR
PATH

FTPDATA CLIENT

  SECURE_MECHANISM  TLS
  TLSRFCLEVEL       RFC4217
  TLSMECHANISM      ATTLS    ; connect at TLS 1.2 or higher
  SECURE_FTP        REQUIRED
  SECURE_CTRLCONN   CLEAR    ; Commands may be clear (unencrypted).
  SECURE_DATACONN   PRIVATE  ; Payload must be encrypted.
  EPSV4             TRUE

FTPDATA CLIENT DEBUG

DEBUG SEC
DEBUG TIM
DEBUG BAS
DEBUG FLO
DEBUG ALL

### FTP to JES:
open hostname
userid
password
prompt off
quote site file=jes
dir

SITE / LOCSITE / QUOTE SITE / CALL SITE

SITE VARrecfm LRECL=32760 RECFM=U BLKSIZE=32760

quote site:
JESJOBNAME
JESSTATUS
JESOWNER
--------------------------------

# SSH

```
ssh -vvv -c aes256-cbc -p 8022 8.8.8.8
sftp -c aes256-cbc -P 8022 8.8.8.8
Sftp -o "StrictHostkeyChecking no"
```

SFTP

https://www.ibm.com/docs/en/zos/2.4.0?topic=guide-accessing-mvs-data-sets-within-sftp
https://www.ibm.com/docs/en/zos/2.1.0?topic=utility-invoking-bpxbatch-in-batch-job

```
# sftp -h
usage: sftp Ý-46aCfpqrv¨ Ý-B buffer_size¨ Ý-b batchfile¨ Ý-c cipher¨
          Ý-D sftp_server_path¨ Ý-F ssh_config¨ Ý-i identity_file¨ Ý-l limit¨
          Ý-o ssh_option¨ Ý-P port¨ Ý-R num_requests¨ Ý-S program¨
          Ý-s subsystem | sftp_server¨ host
       sftp Ýuser@¨hostÝ:file ...¨
       sftp Ýuser@¨hostÝ:dirÝ/¨¨
       sftp -b batchfile Ýuser@¨host
```

https://www.ibm.com/docs/en/zos/2.2.0?topic=ssftp-options

https://www.ibm.com/docs/en/zos/2.2.0?topic=program-host-key-checking

https://www.ibm.com/docs/en/integration-bus/10.0?topic=sftp-known-host-checking

SSH

```
usage: ssh Ýoptions¨ Ýuser@¨host Ýcommand¨
Options:
  -4          Use IPv4 addresses only.
  -6          Use IPv6 addresses only.
  -A          Enables authentication agent forwarding.
  -a          Disables authentication agent forwarding (default).
  -C          Enables compression.
  -f          Fork into background after authentication.
  -G          Causes ssh to print its configuration after evaluating Host and Ma
tch blocks and exit.
  -g          Allow remote hosts to connect to local forwarded ports.
  -K          Enables forwarding (delegation) of GSSAPI credentials to the serve
r.
  -k          Disables forwarding (delegation) of GSSAPI credentials to the serv
er.
  -M          Places the ssh client into master mode for connection sharing.
  -N          Do not execute a shell or command.
  -n          Redirect input from /dev/null.
  -q          Quiet mode; suppress most warning and diagnostic messages.
    -q          Quiet mode; suppress most warning and diagnostic messages.
  -s          Invoke command (mandatory) as SSH2 subsystem.
  -T          Disables pseudo-tty allocation.
  -t          Force pseudo-tty allocation.
  -V          Display version number only.
  -v          Verbose mode; display verbose debugging messages.
              Multiple -v increases verbosity.
  -X          Enables X11 connection forwarding.
  -x          Disables X11 connection forwarding (default).
  -Y          Enables trusted X11 forwarding.
  -y          Send log information to syslog.
  -b addr     Local IP address.
  -c cipher   Select encryption algorithm.
  -D Ýbind-addr:¨port     Enables dynamic application-level port forwarding.
  -e char     Set escape character; ``none'' = disable (default: ~).
  -E file     Append debug logs to file instead of standard error.
  -F config   Config file (default: ~/.ssh/config).
  -i file     Identity for public key authentication.
  -J Ýuser@¨hostÝ:port¨¨     Shortcut to specify a ProxyJump configuration direc
tive.
tive.
  -L Ýbind_address:¨port:host:hostport   Forward local port to remote address.
  -L Ýbind_address:¨port:remote_socket   Forward local port to remote socket.
  -L local_socket:host:hostport          Forward local socket to remote address.
  -L local_socket:remote_socket          Forward local socket to remote socket.
  -l user     Log in using this user name.
  -m macs     Specify MAC algorithms.
  -O ctl-cmd  Control an active connection multiplexing master process.
  -o 'option' Process the option as if it was read from a configuration file.
  -p port     Port to connect to on the remote host.
  -Q cipher | cipher-auth | mac | kex | key | key-cert | key-plain | protocol-ve
rsion   Queries ssh for the supported algorithms.
  -R Ýbind_address:¨port:host:hostport   Forward remote port to local address.
  -R Ýbind_address:¨port:local_socket    Forward remote port to local socket.
  -R remote_socket:host:hostport         Forward remote socket to local address.
  -R remote_socket:local_socket          Forward remote socket to local socket.
  -R Ýbind_address:¨port                 Forward remote port to using SOCKS.
  -S ctl-path Specifies the location of a control socket for connection sharing.
  -W host:port   Requests that client standard input and output be forwarded.

ssh -Q mac and ciphers
```

KEYSCAN

```
ssh-keyscan -H -t rsa 8.8.8.8  >> ~/.ssh/known_hosts
```

```
# ssh-keyscan -h
unknown option -- h
usage: ssh-keyscan Ý-46cHv¨ Ý-f file¨ Ý-p port¨ Ý-T timeout¨ Ý-t type¨
                   Ýhost | addrlist namelist¨ ...
```

KEYGEN

```
ssh-keygen -t rsa
ssh-keygen -t dsa
```

```
ssh-keygen -i -f testkey.putty.pub >>  /USERIDHOME/.ssh/authorized_keys
```

zOS Open SSH uses BASE64 encoding. 


BE CAREFUL on how it is uploaded. When you upload a key file, it might get encoded in a different way.
ssh-keygen -i -m RFC4716 -f /u/user/pub >>  /u/user/pubibm

```
ssh-keygen help
```

```
usage: ssh-keygen Ýoptions¨
  ssh-keygen Ý-q¨ Ý-b bits¨ Ý-t type¨ Ý-o¨ Ý-a rounds¨ Ý-N new_passphrase¨ Ý-C comment¨ Ý-f output_keyfile¨
  ssh-keygen -p Ý-P old_passphrase¨ Ý-N new_passphrase¨ Ý-f keyfile¨
  ssh-keygen -i Ý-m key_format¨ Ý-f input_keyfile¨
  ssh-keygen -e Ý-m key_format¨ Ý-f input_keyfile¨
  ssh-keygen -e Ý-m key_format¨ Ý-f input_keyfile¨
  ssh-keygen -y Ý-f input_keyfile¨
  ssh-keygen -c Ý-P passphrase¨ Ý-C comment¨ Ý-f keyfile¨
  ssh-keygen -l Ý-v¨ Ý-E fingerprint_hash¨ Ý-f input_keyfile¨
  ssh-keygen -B Ý-f input_keyfile¨
  ssh-keygen -F hostname Ý-f known_hosts_file¨ Ý-l¨
  ssh-keygen -H Ý-f known_hosts_file¨
  ssh-keygen -R hostname Ý-f known_hosts_file¨
  ssh-keygen -r hostname Ý-f input_keyfile¨ Ý-g¨
  ssh-keygen -G output_file Ý-v¨ Ý-b bits¨ Ý-M memory¨ Ý-S start_point¨
  ssh-keygen -T output_file -f input_file Ý-v¨ Ý-a rounds¨ Ý-J num_lines¨ Ý-j start_line¨ Ý-K checkpt¨ Ý-W generator¨
  ssh-keygen -s ca_key -I certificate_identity Ý-h¨ Ý-U¨ Ý-n principals¨ Ý-O option¨ Ý-V validity_interval¨ Ý-z serial_number¨ file
...
  ssh-keygen -L Ý-f input_keyfile¨
  ssh-keygen -A
  ssh-keygen -k -f krl_file Ý-u¨ Ý-s ca_public¨ Ý-z version_number¨ file ...
  ssh-keygen -Q -f krl_file file ...
Options:
  -A          Generate non-existent host keys for all key types.
  -a rounds   Number of KDF rounds used or number of tests for screening DH-GEX moduli (with -T).
  -B          Show bubblebabble digest of key file.
  -b bits     Number of bits in the key to create.
 -C comment  Provide new comment.
 -c          Change comment in private and public key files.
 -d          Same as '-t dsa'; Specifies dsa type key.
 -E          Display key fingerprints using hash algorithm: md5 |sha256
 -e | -x     Export OpenSSH to foreign format key file.
 -F hostname Find hostname in known hosts file.
 -f filename Filename of the key file.
 -G file     Generate candidates for DH-GEX moduli.
 -g          Use generic DNS resource record format.
 -H          Hash names in known_hosts file.
 -h          Generate host certificate instead of a user certificate.
 -I key_id   Key identifier to include in certificate.
 -i | -X     Import foreign format to OpenSSH key file.
 -J number   Screen this number of moduli lines.
 -j number   Start screening moduli at specified line.
 -K checkpt  Write checkpoints to this file.
 -k          Generate a KRL file.
 -L          Print the contents of a certificate.
 -l          Show fingerprint of key file.
 -M memory   Amount of memory (MB) to use for generating DH-GEX moduli.
 -m key_fmt  Conversion format for -e/-i (PEM|PKCS8|RFC4716).
 -N phrase   Provide new passphrase.
 -n name,... User/host principal names to include in certificate
 -O option   Specify a certificate option.
-o          Save private keys using the new OpenSSH format.
-P phrase   Provide old passphrase.
-p          Change passphrase of private key file.
-Q          Test whether key(s) are revoked in KRL.
-q          Quiet.
-R hostname Remove host from known_hosts file.
-r hostname Print DNS resource record.
-S start    Start point (hex) for generating DH-GEX moduli.
-s ca_key   Certify keys with CA key.
-T file     Screen candidates for DH-GEX moduli.
-t type     Specify type of key to create: dsa | ecdsa | ed25519 | rsa
-U          Indicates that a CA key resides in a ssh-agent.
-u          Update KRL rather than creating a new one.
-V from:to  Specify certificate validity interval.
-v          Verbose.
-W gen      Generator to use for generating DH-GEX moduli.
-y          Read private key file and print public key.
-z serial   Specify a serial number.
```

Configuration File:

```
Host hostname
   Port 22
   IdentityFile ~/.ssh/id_rsa
```

Start from UNIX:

```
# Start the SSH daemon                                                       
_BPX_JOBNAME='SSHD' /usr/sbin/sshd -f /etc/ssh/sshd_config 2>/dev/console &  
```                                                                             
   
```   
# Start the sftp daemon                                                      
_BPX_JOBNAME='SSHDF' /usr/sbin/sshd -f /etc/ssh/sftpd_config 2>/dev/console &
```
  
https://askubuntu.com/questions/123072/ssh-automatically-accept-keys
https://serverfault.com/questions/638600/auto-accept-rsa-key-fingerprint-from-command-line
https://stackoverflow.com/questions/21383806/how-can-i-force-ssh-to-accept-a-new-host-fingerprint-from-the-command-line#comment108409638_53672867
https://www-01.ibm.com/servers/resourcelink/svc00100.nsf/pages/zOSV2R4sc276806/$file/foto100_v2r4.pdf
https://www.ibm.com/support/pages/example-batch-sftp-script
https://www.ibm.com/docs/en/zos/2.3.0?topic=administrators-starting-sshd-daemon
https://www.ibm.com/docs/en/zos/2.3.0?topic=SSLTBW_2.3.0/com.ibm.zos.v2r3.foto100/bpxstart.htm
https://www.ibm.com/docs/en/zos/2.3.0?topic=SSLTBW_2.3.0/com.ibm.zos.v2r3.foto100/fotz118.htm
https://www.ibm.com/docs/en/zos/2.3.0?topic=SSLTBW_2.3.0/com.ibm.zos.v2r3.foto100/fotz117.htm
https://www.ibm.com/docs/en/zos/2.3.0?topic=daemon-restarting-sshd-without-bringing-it-down
https://www.ibm.com/docs/en/zos/2.2.0?topic=descriptions-zos-openssh
https://www.ibm.com/docs/en/zos/2.3.0?topic=daemon-ways-start-sshd-as-stand-alone

-----------------------------------------------------------------------------------------------------------------------------
-----------------------------------------------------------------------------------------------------------------------------
-----------------------------------------------------------------------------------------------------------------------------

# RACF

## Common

```
TSO LU
TSO LU OMVS NORACF
TSO RACDCERT ID(*) LIST(LABEL())
TSO RACDCERT ID(*) LISTCERT(*)
TSO RACDCERT ID(*) LISTCHAIN(LABEL())
```

```
TSO RVARY LIST           / BASES
TSO RACDCERT ID(TCPIP) LIST(LABEL('ROOT'))
TSO RACDCERT ID(userid) LISTring(ring)
TSO RACDCERT SITE LIST(LABEL'ASD'))
```

http://www.redbooks.ibm.com/redbooks/pdfs/sg248041.pdf

```
RACF 0207 RECORD TYPE - grabs all types of certs: CERTAUTH
RACDCERT CERTAUTH LIST
RACDCERT SITE LIST
```

CHECK CERTIFICATE ON DSN:

```
racdcert checkcert('HLQ.CERT') password('pass')
```

Tsolib activate uncond ddname=('zdp.load')

## Certificates

### RACF INSERT CERTIFICATE:

```
RACDCERT CERTAUTH ADD('dataset') TRUST +
WITHLABEL('label')
```

### RACF REMOVE FROM RING:

```
RACDCERT ID(id) REMOVE(CERTAUTH LABEL('label') RING(ringname)
```

EXPORT CERTAUTH CERT:

```
//SYSTSIN DD DATA
RACDCERT EXPORT(LABEL('CERTLABEL')) -
CERTAUTH DSN(HLQ.CERT)
/*
```

https://www.ibm.com/docs/en/zos/2.1.0?topic=syntax-racdcert-export-export-certificate-package

EXPORT PERSONAL CERT:

```
//SYSTSIN DD DATA
RACDCERT EXPORT(LABEL('CERTLABEL')) -
ID(IBMTCP) DSN(HLQ.CERT)
/*
```

Self Signed Certificate Creation:

```
RACDCERT ID(user) GENCERT +
    SUBJECTSDN(CN('certcn')) +
    WITHLABEL('certlabel') +
    SIGNWITH(CERTAUTH LABEL('rootlabel')) +
    NOTAFTER(DATE(date))
```

TRUST Certificate:

```
RACDCERT ALTER(LABEL('certlabel'))  +
    ID(TCPIP) TRUST
```

CONNECT Certificate to Ring:

```
RACDCERT ID(TCPIP) +
   CONNECT(ID((user) LABEL('certlabel') +
   RING(ringname)
  SETROPTS RACLIST(DIGTCERT, DIGTRING) REFRESH
```

Full Certificate Connect Process with RDATALIB Creation:

```
RACDCERT ID(user) ADDRING(ringname)                          
RACDCERT ID(user) CONNECT(SITE LABEL('certlabel') +       
RING(ringname) USAGE(PERSONAL) DEFAULT                          
RACDCERT ID(user) CONNECT(CERTAUTH LABEL('intcalabel') +  
RING(ringname) USAGE(CERTAUTH)                                  
RACDCERT ID(user) +                                          
CONNECT(CERTAUTH LABEL('rootcalabel') +       
RING(user) USAGE(CERTAUTH)                               
RDEF RDATALIB user.ringname.LST OWN(RESOURCE)               
PE user.ringname.LST CL(RDATALIB) ID(user,user2) AC(C)    
SETR REFRESH RACLIST(RDATALIB)                                 
RACDCERT ID(user) LISTRING(*)                                  
RL RDATALIB user.ringname.LST AUTH    
```

-----------------------------------------------------------------------------------------------------------------------------
-----------------------------------------------------------------------------------------------------------------------------
-----------------------------------------------------------------------------------------------------------------------------

# ACF2

## Usual

T PROF(USER) DIV(KEYRING)
T PROF(USER) DIV(CERTDATA)
LIST USERID.RING
LIST USERID.CERT

T RES(FAC)
L IRR
t res(fac)
t res(rda)
l user
chkcert
set profile(user) div(omvs)                                                   
list uid

ACF2 LIST ALL RINGS:
T PROF(USER) DIV(KEYRING)
LIST LIKE(-)

ACF2 LIST ALL CERTS:
T PROF(USER) DIV(CERTDATA)
LIST LIKE(-)

omvs
Keyring
CERTDATA

Chkcert 

ACF2
CHKCERT certificaterecord CHAIN - will show the certificate chain

ACF2
CHKCERT DSN('frank01.mycert') password('pass')

F ACF2,REBUILD(usr),class(p)                                      
F ACF2,OMVS 
F ACF2,RESET(UID)


F ACF2,REBUILD(USR),CLASS(P) 
F ACF2,OMVS(CERTDATA) 
F ACF2,REBUILD(FAC)

## ACFCERT

CHA keyringdata DEFAULT(certdata)

INSERT USING(oldring) newring

$KEY(USERID) TYPE(RDA)
 RINGNAME.LST UID(UID) SERVICE(READ) ALLOW

$KEY(IRR) TYPE(FAC)
 DIGTCERT.LIST UID(ID) SERVICE(READ) ALLOW
 DIGTCERT.LISTRING UID(ID) SERVICE(READ,UPDATE) ALLOW

$KEY(APPLID) TYPE(APL)
 UID(ID) ALLOW

https://www.ibm.com/docs/en/zos/2.1.0?topic=gime-importing-certificate-from-file-as-trusted-ca-certificate

https://techdocs.broadcom.com/us/en/ca-mainframe-software/security/ca-acf2-for-z-os/16-0/administrating/digital-certificate-support.html

https://techdocs.broadcom.com/us/en/ca-mainframe-software/security/ca-acf2-for-z-os/16-0/administrating/digital-certificate-support/process-digital-certificates-with-ca-acf2.html

https://knowledge.broadcom.com/external/article/18198/does-acf2-support-virtual-keyrings.html

https://knowledge.broadcom.com/external/article/94292/how-do-we-specify-keyring-name-in-a-batc.html


----------------------------------------------------------------------------------------------------------
----------------------------------------------------------------------------------------------------------
----------------------------------------------------------------------------------------------------------

# JCL

#### REUSABLE

https://www.ibm.com/docs/en/zos-basic-skills?topic=sample-reusable-jcl-deleting-some-vsam-clusters

FileAid

https://docs.bmc.com/docs/bcfamvs/2101/sample-jcl-statements-1014793496.html

https://www.techagilist.com/mainframe/jcl/fileaid-in-batch-mode-with-examples/

SDSF Commands over batch:

https://www.ibm.com/docs/en/zos/2.1.0?topic=reference-jcl-command-statement

https://www.ibm.com/docs/en/zos/2.3.0?topic=d-syntax-7

https://www.ibm.com/docs/en/zos/2.3.0?topic=d-examples-command-statement

https://www.ibm.com/docs/en/zos/2.3.0?topic=batch-invoking-sdsf-in

--------------------------------------------

#### Parameters

DCB:

https://www.ibm.com/docs/en/zos/2.1.0?topic=parameter-examples-dcb

https://www.ibm.com/docs/en/zos/2.2.0?topic=dp-syntax-2

https://www.ibm.com/docs/en/zvm/7.2?topic=reference-device-characteristics

https://ibmmainframes.com/references/disk.html

https://www.ibm.com/docs/en/zos/2.2.0?topic=requirements-step-1-number-tracks-required

//DD1 DD DSNAME=ALP,DISP=(,KEEP),VOLUME=SER=44321, // UNIT=3400-6,DCB=(RECFM=FB,LRECL=240,BLKSIZE=960, // DEN=1,TRTCH=C)

1 Cyl = 15 Tracks 
1 Track = 25 Blocks

1 Cylinder = 55,996 * 15  =  839,940 bytes.
so 1000 cylinders = 839,940 * 1000   
1 Megabyte =  1,048,576 (2 to the 20th power) bytes.
1000 cylinders = (839,940 * 1000 ) / 1,048,576  = 801.029 MB
1 terabyte =  2 to the 40th power or approximately a thousand billion bytes (that is, a thousand gigabytes).
1000 cylinders = (839,940 * 1000 ) / (1,048,576 * 1,048,576 )  = .000763 Terabytes

SET statement

https://www.ibm.com/docs/en/zos/2.1.0?topic=description-examples-set-statement

TYPRUN

https://www.ibm.com/docs/en/zos/2.2.0?topic=parameter-example-typrun

https://www.ibm.com/docs/en/zos/2.2.0?topic=statement-typrun-parameter
S PROC,TYP=EXEC 

-----------------------------------------------------------------------------------------------------------------------------
-----------------------------------------------------------------------------------------------------------------------------

#### FileAid

https://docs.bmc.com/docs/bcfamvs/2101/sample-jcl-statements-1014793496.html
https://www.techagilist.com/mainframe/jcl/fileaid-in-batch-mode-with-examples/

--------------------------------------------

#### SDSF
https://www.ibm.com/docs/en/zos/2.1.0?topic=reference-jcl-command-statement
https://www.ibm.com/docs/en/zos/2.3.0?topic=d-syntax-7
https://www.ibm.com/docs/en/zos/2.3.0?topic=d-examples-command-statement
https://www.ibm.com/docs/en/zos/2.3.0?topic=batch-invoking-sdsf-in

--------------------------------------------

#### BPXBATCH:

https://www.ibm.com/docs/en/zos/2.1.0?topic=utility-invoking-bpxbatch-in-batch-job
https://www.ibm.com/docs/en/zos/2.1.0?topic=command-entering-long-shell
https://www.ibm.com/docs/en/zos/2.1.0?topic=job-example-running-shell-command-in-batch
https://www.ibm.com/docs/en/zos/2.1.0?topic=bpxbatch-ways-define-stdparm
https://www.ibm.com/docs/en/zos/2.1.0?topic=utility-passing-parameter-data-bpxbatch#batstdparm

-----------------------------------------------

#### REXX

https://ibmmainframes.com/about51007.html
https://www.ibm.com/docs/en/zos/2.1.0?topic=ir-using-irxjcl-run-rexx-exec-in-mvs-batch
https://www.ibm.com/docs/en/zos/2.1.0?topic=routine-exec-block-execblk

-----------------------------------------------

#### VSAM:

Use IDCAMS.

REPRO to create another. Use LIKE to replicate.
DELETE
LISTCAT ALL ENTRIES(DATASET-NAME) 

https://www.ibm.com/docs/en/zos/2.4.0?topic=de-delete-key-sequenced-vsam-cluster-in-catalog-example-6
https://www.ibm.com/docs/en/zos/2.4.0?topic=de-delete-key-sequenced-vsam-cluster-in-catalog-example-6
https://www.ibm.com/docs/en/zos-basic-skills?topic=sample-reusable-jcl-deleting-some-vsam-clusters


----------------------------------------------

#### SMPE

HTTPS

```
 <ORDERSERVER
    inventory="all"
    url="https://ws-prod.bmc.com/smpe"
    keyring="USERID/RINGNAME"
    certificate="BMC CERT">
 </ORDERSERVER>
//SMPCLNT DD *
 <CLIENT
    javahome="/usr/lpp/java/J8.0_64"
    classpath="/usr/lpp/smp/classes"
    downloadmethod="https"
    downloadkeyring="javatruststore">
 </CLIENT>
 ```

RACF RING: 
keyring="USERID/RINGLABEL"

ACF2 RING:
keyring="USERID/RINGLABEL"

USER.RING  LABEL=RINGNAME
keyring="USER/RINGNAME"


FTP

```
 <CLIENT>                                           
  <FTPOPTIONS>                                     
    -d -v -f "//'FTPDATADATASET'"
  </FTPOPTIONS>                                    
</CLIENT>   
```

-----------------------------------------------------------------------------------------------------------------------------
-----------------------------------------------------------------------------------------------------------------------------

#### EXAMPLES

SDSF Commands:

```
//STEP01 EXEC PGM=SDSF,PARM='++30,256'
//ISFOUT   DD SYSOUT=*
//SYSUDUMP DD SYSOUT=*
//SYSPRINT DD SYSOUT=*
//SYSTSPRT DD SYSOUT=*
//SYSOUT   DD SYSOUT=*
//DATAOUT  DD DSN=HLQ.QL,
//            DISP=(SHR,KEEP,KEEP)
//ISFIN    DD *
SET CONSOLE BATCH
SET DELAY 100
/D IPLINFO
/D M=CPU
/D XCF
/D SYMBOLS
/D NET,ID=VTAM
/D NET,CPCP
/D NET,VTAMOPTS
/D TCPIP,,N,HOME
/D TCPIP,,N,DEV
/D TCPIP,,N,CONFIG
/D TCPIP,,N,ROUTE
/D TCPIP,,N,CONN,MAX=*
/D TCPIP,,OMPROUTE,OSPF,LIST,ALL
/D NET,TRL
/D NET,CDRMS
/D NET,TOPO,LIST=ALL
/D TCPIP,,OSAINFO,INTFNAME=OSA
/D TCPIP,,N,VIPADCFG,DETAIL
PRINTFILE DATAOUT
ULOG
PRINT
PRINT CLOSE
END
```

IEBCOPY - Copy MODULEs

```
//STEP1    EXEC PGM=IEBCOPY
//SYSPRINT DD  SYSOUT=*
//MEMIN    DD DSN=HQL.QL(MEMBER),
//         DISP=SHR
//MEMOUT   DD DSN=HLQ.QL2(MEMBER),
//         DISP=SHR
//SYSIN    DD *
COPYOPER   COPY    OUTDD=MEMOUT
                   INDD=MEMIN
           SELECT  MEMBER=((MEMBER,,R))
```

ADRDSSU

```
//DUMP     EXEC PGM=ADRDSSU
//SYSPRINT DD SYSOUT=*
//DDOUT    DD DSN=SHRSYS.IODF.DMP1,DISP=(,CATLG),
//         SPACE=(CYL,(100,100),RLSE),UNIT=3390
//SYSIN    DD *
  DUMP                                     -
      OUTDDNAME(DDOUT)                     -
     DATASET(INCLUDE(IODF.CLUSTER)) -
  TOL(ENQF)
/*
```
		   
IDCAMS - COPY to GDG

```
//STEP2    EXEC PGM=IDCAMS
//SYSPRINT DD  SYSOUT=*
//IN       DD DSN=HLQ.QL,
//         DISP=SHR
//OUT      DD DSN=HLQ.GDGBASE(+1),
//         DISP=(NEW,CATLG,),
//         SPACE=(TRK,(15,10)),
//         DCB=(BLKSIZE=27920,LRECL=80,RECFM=FB)
//SYSIN    DD *
   REPRO IFILE(IN) OFILE(OUT) REPLACE
/*
```

GDG BATCH

```
//STEP1    EXEC PGM=IDCAMS
//SYSPRINT DD SYSOUT=*
//SYSIN    DD *
 DEFINE GDG(NAME(HLQ.GDGBASE) -
 LIMIT(10) -
 NOEMPTY -
 SCRATCH)
```

FTP BATCH

```
//FTP1A    EXEC PGM=FTP,COND=(0,NE),REGION=0M,
//* Choose the remote host on PARM and port (after a space)
//         PARM='hostname (EXIT TIMEOUT 720'
//* You can use a NETRC to grab the credentials
//* If you are using NETRC you don't need to input user and password
//NETRC    DD  DISP=SHR,DSN=HLQ.QL(NETRC)
//SYSPRINT DD SYSOUT=*
//* You can use a different FTPDATA file for the transfer
//SYSFTPD  DD  DISP=SHR,DSN=HLQ.QL(FTPDATA)
//OUTPUT   DD SYSOUT=*
//INPUT    DD DUMMY
Ls
```

NETRC:
machine iphostname login user password pass


FTPS BATCH (WITHOUT AT-TLS)

```
//FTP1A    EXEC PGM=FTP,COND=(0,NE),REGION=0M,
//* Choose the remote host on PARM and port (after a space)
//         PARM='hostname (EXIT TIMEOUT 720'
//* You can use a NETRC to grab the credentials
//* If you are using NETRC you don't need to input user and password
//CCEEOPTS DD *
ENVAR('GSK_PROTOCOL_TLSV1_2=1',
GSK_V3_CIPHER_SPECS=3D39383735)
//NETRC    DD  DISP=SHR,DSN=HLQ.QL(NETRC)
//SYSPRINT DD SYSOUT=*
//* You can use a different FTPDATA file for the transfer
//SYSFTPD  DD  DISP=SHR,DSN=HLQ.QL(FTPDATA)
//OUTPUT   DD SYSOUT=*
//INPUT    DD DUMMY
Ls
```


IKJEFT1B - EXECUTE REXX from external Library

```
//REPOFTP   EXEC PGM=IKJEFT1B,TIME=1439                                          
//SYSEXEC   DD  DISP=SHR,DSN=HLQ.QL                                 
//SYSTSPRT  DD  SYSOUT=*                                                        
//SYSTSIN   DD  *                                                               
  %REXXMEM                                                                     
/*   
```

IKJEFT01 - TSO EXEC

```
//TSOEX     EXEC PGM=IKJEFT01                                                   
//SYSEXEC   DD DSN=HLQ.QL,DISP=SHR                                   
//SYSTSPRT  DD SYSOUT=*                                                         
//SYSPRINT  DD SYSOUT=*                                                         
//SYSTSIN   DD *                                                                
  EXEC 'HLQ.QL(REXXMEM)'                                              
//     
```

IPCS BATCH

```
//SNIFFER  EXEC PGM=IKJEFT01,DYNAMNBR=50
//STEPLIB  DD  DISP=SHR,DSN=SYS1.MIGLIB
//IPCSPARM DD  DISP=SHR,DSN=SYS1.PARMLIB
//         DD  DISP=SHR,DSN=SYS1.IBM.PARMLIB
//IPCSDDIR DD  DISP=SHR,DSN=HLQ.IPCS
//SYSPROC  DD  DISP=SHR,DSN=SYS1.SBLCLI0
//SYSTSPRT DD  SYSOUT=*
//IPCSTOC  DD  SYSOUT=*
//IPCSPRNT DD  SYSOUT=*
//SNIFFER  DD  DSN=HLQ.SNIFFER,DISP=(NEW,CATLG),
//                             UNIT=3390,RETPD=30,SPACE=((CYL,(100,100)),
//                             DCB=(RECFM=VB,LRECL=27994,BLKSIZE=0)
//*
//SYSTSIN       DD *
  IPCS
  CTRACE DSN('HLQ.CTTRACE') -
        COMP(SYSTCPDA) SUB(TCPIP)) FULL -
        OPTIONS((PACKETTRACE SNIFFER(27956 ETHERNET) NOREASSEMBLY STATS))
  END
```

PING BATCH

```
//STEP01    EXEC  PGM=IKJEFT01
//SYSTSPRT  DD  DISP=SHR,DSN=output
//SYSTSIN   DD  *
PING 8.8.8.8
```

SFTP BATCH

```
//SFTPSTEP  EXEC PGM=BPXBATCH
//SYSPRINT  DD SYSOUT=*
//STDOUT    DD SYSOUT=*
//STDERR    DD SYSOUT=*
//STDPARM   DD *
sh sftp -P port
-o "StrictHostKeyChecking no"
userid@server
```

SMTP

When sending Attachments, SYSUT1 needs to be in a dataset and it has to have the same LRECL as the file you 
are attaching

```
//SMTPTEST  EXEC PGM=IEBGENER                       
//SYSPRINT  DD  SYSOUT=*                            
//SYSUT2    DD  SYSOUT=(B,SMTP)                     
//SYSIN     DD  DUMMY                               
//SYSUT1    DD  *                                   
HELO sysname                                          
MAIL FROM:MAINFRAME@youraccount.COM             
RCPT TO:yourmail@youraccount.COM       
RCPT TO:yourseniormail@youraccount.COM                  
DATA                                               
FROM: MAINFRAME                                    
TO:yourmail@youraccount.COM       
TO:yourseniormail@youraccount.COM                  
SUBJECT: TEST                                      
MIME-VERSION: 1.0                                  
CONTENT-TYPE: TEXT/PLAIN                           
CONTENT-DISPOSITION: ATTACHMENT; FILENAME=TEST.TXT 
//     DD DISP=SHR,DSN=yourdataset
```

NOTE: make sure the Record Format and Record Length are the same between the PDS in which you have this member and "yourdataset" DCB parameters.      

https://www.ibm.com/support/pages/outbound-email-attachments-using-smtp-or-cssmtp-zos




---------------------------------------------------------------
---------------------------

# Useful

## XEQ

$DN,Q=XEQ
$P XEQ
QUIT XEQ nodename
$S XEQ

JCL:
/*XEQ nodename

--------------------------------------------

## curl

// on Windows
curl.exe -H "Content-Type:application/json" -d "{'text':'Hello World'}" <YOUR WEBHOOK URL>

// on macOS or Linux
curl -H 'Content-Type: application/json' -d '{"text": "Hello World"}' <YOUR WEBHOOK URL>

--------------------------------------------

COPY /etc/ and /var/

cp -r /etc/ /u/users/user/etc
diff -R /etc/ /u/users/user/etc/

--------------------------------------------

SETPROG 
LLA REFRESH

--------------------------------------------

VMCF:
F VMCF,DISPLAY,NAME=*
F TNF,DISPLAY,NAME=*
F VMCF,REMOVE,NAME=*
F TNF,REMOVE,NAME=*
PROCLIB()

--------------------------------------------

ISPF Commands
=x
=xall
x all
f str

Remove all lines:
x all
f asssdsad all
x '//*' all

Command line on Top:
ISPF - Main Panel - Option 0 - Command line on Bottom

--------------------------------------------

UTILS:
Copy PDS - CO / S *
Save in View Mode: rep .zf .zl samemembername

--------------------------------------------

Check VTOC config:
In 3.4 put the Volume Serial 
Put a v in the command line

--------------------------------------------

DB2
db2 catalog tcpip node DB2SYSTEM remote HOSTNAME server 5002 
db2 catalog dcs database DB2SYSTEM_SYS as DB2SYSTEM_SYSTEM 
db2 catalog database DB2SYSTEM_SYS as DB2SYSTEM_SYS at node DB2SYSTEM authentication server_encrypt

--------------------------------------------

DUMPS:
D D,L - will tell you the available dump datasets

dump comm=(high CPU) - (tcpip cpu)
r xx,jobname=(TCPIP),sdata=(RGN,CSA,PSA,TRT,LSQA),end

--------------------------------------------

SDSF:

PRINT
PRINT CLOSE
XDC

IOF:

SD
N next to output
SNAPCLOS

SD DSN('HLQ.MEMBER')
CAPTURE ROWS(4000) COLS(512)
SNAPCLOS

IOF
https://www.triangle-systems.com/doc/7j/UG7JC13.HTM
https://www.fisc.com/support/docs/IOF@8FUserGuide16.pdf

SD
N NEXT TO JOB
SNAPCLOS

LONG - Extended command

IOF
ed - edit JCL

SDSF 
sj - edit JCL

IOF SDSF PANEL
SN - Start node
DL - Dsiaply Node status
DC - Display connect information
DP - Display Path information

 ISPF PANEL:
 https://www.ibm.com/docs/en/zos/2.1.0?topic=services-browse-browse-data-set
 https://share.confex.com/share/117/webprogram/Handout/Session9764/S9764%20-%20ISPF%20Panels%20Advanced.pdf
 ISPCMDS

 PANELID - Will show the Panel ID and you can invoke it 

ISPF How to know what is the panel you are on:
PANELID ON - Will show the Panel ID to invoke

http://www.techtricky.com/useful-list-of-tso-ispf-commands/
http://www.techtricky.com/iebcopy-in-jcl-with-examples/
https://ibmmainframes.com/about64370.html

1) To view the structure (details like starting position, end position, length and type of fields) of a copybook – This can be viewed from FILEAID option 8.

2) To Copy a member from one PDS to Another:

Open the first PDS using 3.4, and type C before the member and ENTER it will ask for the target PDS name, there give the PDS name.It will be copied by creating the Member with same name.

3) To copy one entire PDS to another New PDS

Open the source PDS using 3.4 option, and type CO before PDS name, then it will ask for the target PDS, Give the target PDS, it creates and copies the source to Target.

Note: Once you give the CO and press enter it displays all the members in that PDS. There you can select the members you want to copy by giving the S before to that member.If you want to copy all the members give S * in the command line then it selects all the members in that PDS.

4) In TSO to search a member from all of your PDS’s

Go to 3.4 Type one PDS in your list
Append all your PdS in your list by using Append command
Type MEM “MBR Name” in the command line.
The result will show the datasets contains that particular member.

5) If you want to find all the members contain a particular string, Then

Open the PDS using 3.4
Type SRCHFOR ‘string’ in the command line.
It shows all the members containing that string(press enter by putting the cursor on the PROMPT )
6) TSO ISPVCALL STATUS to view the version of the system software.

In SPOOL give the command /d prod. It gives the versions of system and sub systems.

7) TSO command to find the latest version of the GDG.

TSO LISTCAT LVL(GDG.BASE)

8) While trying to open any member in a PDS, we sometimes come across

“member in use” message. In that situation, if you want to know who is using the member currently, press F1 twice.

9) Suppose you are in a ISPF Screen and want to know in which TSO Region ( Development, Production, or other TSO regions) you are now .

Issue on the command line : SAREA

10) To find the last datasets that you have accessed.

GO TO ISPF 3.4 option.
On the top, there is a MENUBAR. Select REFLIST
Select Option 1 in it.
Using this option you can find out the last 30 datasets that you have accessed.

11) To replace a string in a Program/member

Type C ALL ‘string1’ ‘string2’

12) To replace a string in a program from specific line number(linenum1) to another line number(linenum2)

– Put .A at linenum1 & .B at linenum2

– Type C ALL ‘string1’ ‘string2’ .A .B

It replaces all string1 with strng2 between the two line numbers(not the entire program)

13) If you open the multiple screens in ISPF, to navigate between those you need to type the below commands:

If you want open the 1st screen type 1 in command line and press F9, for 2nd screen 2 and F9 etc.

If you want to see all the opened screens type LIST and press F9. Type S before the screen you want to open and press enter.

Active ISPF Logical Sessions

. Start a new screen
. Start a new application

Application Name

ID Name Panelid Applid Session Type

S 1 FMDB2 FMN2P2EZ FMN2 3270
. 2* DSLIST ISRUDSM ISR 3270
. 3- ISFPCU41 ISF 3270
14) To purge multiple jobs in SDSF:

Enclose all the jobs that needs to be purged with ‘//’ and ‘//P’ as shown below and press enter which inturn purges all the enclosed spool listings.

NP JOBNAME JobID Owner Prty Queue C Pos SAff ASys Status 
//  JB001A JBU00001 USER 1 PRINT 3117 
    JB001A JBU00002 USER 1 PRINT 3118 
    JB001B JBU00003 USER 1 PRINT 3119
//P JB001C JBU00004 USER 1 PRINT 3122

15) ISPF Log can be view from Option 7.5 . It gives the latest performed operations.

 Command ===> Scroll ===> CSR 
********************************* Top of Data **********************************
Time *** ISPF transaction log *** Us

01:26 Start of ISPF Log - - - - Session # 229 -------------------------
01:30 TSO - Command - - HRECOVER 'MG001A.CMD.SOURCE(MEM001)' 
01:35 Utility - Move/Copy - MG001A.CMD.SOURCE(MEM001)' Copied 
01:35 - to 'MG001A.CMD.BKUP(MEM001)'' 
01:35 Utility - Delete - ''MG001A.CMD.BKUP(MEM002)' deleted from volume PR
01:35 TSO - Command - - %@SDSF 
01:36 TSO - Command - - MAP 
01:37 TSO - Command - - MAPLIST 
01:44 TSO - Command - - COMPARE SESSION 
02:11 TSO - Command - - ISPVCALL STATUS 
******************************** Bottom of Data *********************


--------------------------------------------

/D PARMLIB
/$D PROC
/

--------------------------------------------

INSTALL PRODUCT 
RECEIVE TSO

https://www.ibm.com/docs/en/sia?topic=i-uploading-adapter-package-4
FB
LRECL 80

Use PCOMM Send File

--------------------------------------------

https://www.ibm.com/docs/en/zos/2.1.0?topic=command-displaying-device-status-allocation
D U,VOL=VOLSER
D U{[,deviceclass][,ONLINE ][,[/]devnum[,nnnnn]]                   }
                 [,OFFLINE][,[/]devnum[,nnnnn]]                    
                 [,ALLOC  ][,[/]devnum[,nnnnn]]                                  
                 [,AUTOSWITCH|AS][,[/]devnum[,nnnnn]][SYS=sysname]  
                 [,UNAVAILABLE|UNAVAIL][,[/]devnum[,nnnnn]]      (See Note)
  
   {,IPLVOL}
  
   {,VOL=volser}

   [,L={a|name|name-a}]
   
 CF CHP(id),ONLINE/OFFLINE
V dev,OFFLINE,FORCE (if boxed)
 D M=DEV()
 D M=CPU
 D M=CHP()
 D U,ALL,ONLINE
 
 --------------------------------------------
 

Edx //*

--------------------------------------------

OPUT  mvs_data_set_name | mvs_data_set_name(member_name)
      'pathname'
      BINARY | TEXT
      CONVERT(character_conversion_table | YES | NO)

OGET  'pathname'
      mvs_data_set_name | mvs_data_set_name(member_name)
      BINARY | TEXT
      CONVERT(character_conversion_table | YES | NO)

https://www.ibm.com/docs/en/zos/2.4.0?topic=tc-oput-copy-mvs-data-set-member-into-zos-unix-file
https://www.ibm.com/docs/en/zos/2.4.0?topic=tc-oget-copy-zos-unix-files-into-mvs-data-set

--------------------------------------------

SAR

Recover TAPE 
"no mount authority"
L - enter - JCL created - PF3 and PF3 again, use jobcard and get it mounted

(If on TAPE)
Put an L beside the job and hit enter
PF3 twice
Enter Jobcard and submit
Once the job completes, bago back into SAR and the report will be on disk

----------------------------------------------

UNIX

mv -R directorya directoryb
https://www.ibm.com/docs/en/zos/2.1.0?topic=files-renaming-moving-file-directory

pax -rw /u/users/seba/stuff /u/users/guerra/stuff - it gets copied into /u/users/guerra/stuff
https://www.ibm.com/docs/en/zos/2.4.0?topic=sets-copying-files-within-zos-unix-file-system
https://www.ibm.com/docs/en/zos/2.4.0?topic=descriptions-pax-interchange-portable-archives
https://ibmmainframes.com/about49289.html
https://www.tutorialspoint.com/unix_commands/pax.htm
https://www.computerhope.com/unix/upax.htm


cp copy file
https://www.ibm.com/docs/en/zos/2.4.0?topic=descriptions-cp-copy-file

USS
Copy files 
https://www.ibm.com/docs/en/zos/2.4.0?topic=sets-copying-files-within-zos-unix-file-system
https://www.ibm.com/docs/en/zos/2.4.0?topic=zufs-copying-data-between-zos-unix-file-system-mvs-data-sets
https://www.ibm.com/docs/en/zos/2.4.0?topic=sets-copying-data-using-zos-shell-commands
https://www.ibm.com/docs/en/zos/2.4.0?topic=sets-copying-data-using-tsoe-commands
https://www.ibm.com/docs/en/zos/2.1.0?topic=set-example-using-jcl-ocopy
https://www.ibm.com/docs/en/zos-basic-skills?topic=sample-reusable-jcl-copying-load-module

-----------------------------------------------

TSO LOCATE MODULE

d prog,lnklist
SETPROG LNKLST,DEFINE,NAME=new,COPYFROM=old
SETPROG LNKLST,ADD,NAME=new,DSNAME=HLQ.QL,VOLUME=XXXXXX,ATTOP 
SETPROG LNKLST,ACTIVATE,NAME=new

----------------------------------------------

TSOE:
https://www.ibm.com/docs/en/zos/2.1.0?topic=commands-continuing-command-another-line
https://www.ibm.com/docs/en/zos/2.4.0?topic=syntax-line-continuation

Tsocmd - from shell SSH
https://www.ibm.com/docs/en/zos/2.4.0?topic=scd-tsocmd-run-tsoe-command-from-shell-including-authorized-commands

-----------------------------------------------------

IMS 
https://www.ibm.com/docs/en/ims/15.1.0?topic=commands-display
https://www.ibm.com/docs/en/ims/14.1.0?topic=commands-display-status-command
https://www.ibm.com/docs/en/ims/14.1.0?topic=commands-display-act-command
https://www.ibm.com/docs/en/ims/15.1.0?topic=problems-input-queuing-schedulingtermination-in-dbdc-dcctl-environments
https://www.ibm.com/docs/en/ims/13.1.0?topic=commands-display-node-command
https://www.ibm.com/docs/en/ims/13.1.0?topic=commands-status-attributes-display-command

---------------------------------------------------

List all members
https://ibmmainframes.com/about20083.html
https://ibmmainframes.com/about35401.html
https://ibmmainframes.com/about30765.html


Copy all members
https://ibmmainframes.com/about67133.html
https://www.ibm.com/docs/en/zos/2.3.0?topic=examples-example-1-copy-entire-data-set
https://www.ibm.com/docs/en/zos/2.2.0?topic=ie-example-3-copy-replace-selected-members-data-set
http://www.techtricky.com/iebcopy-in-jcl-with-examples/
http://www.techtricky.com/useful-list-of-tso-ispf-commands/
/ 17 s *

3) To copy one entire PDS to another New PDS

Open the source PDS using 3.4 option, and type CO before PDS name, then it will ask for the target PDS, Give the target PDS, it creates and copies the source to Target.

Note: Once you give the CO and press enter it displays all the members in that PDS. There you can select the members you want to copy by giving the S before to that member.
If you want to copy all the members give S * in the command line then it selects all the members in that PDS.
-------------------------------------

CANCEL
THEN FORCE ARM
THEN FORCE

D A,L
D A,STC - Get Address Space
CANCEL STC
FORCE STC,A=addressspace,ARM
FORCE STC,A=addresspace
If the STC is in STARTING status:
D A,STARTING
CANCEL STARTING,A=addressspace
FORCE STARTING,A=addresspace,ARM
FORCE STARTING,A=addresspace

FORCE ARM
https://www.ibm.com/docs/en/zos/2.4.0?topic=reference-force-command
https://www.ibm.com/docs/en/zos/2.2.0?topic=fc-parameters


STOP TCPIP
/FORCE TCPIP,ARM

--------------------------------------------------------

TSO PRINTDS('HLQ.QL')
TSO PRINT DS('HLQ.QL')

---------------------------------------------------------

IPCS

DEFINE CLUSTER(NAME('userid.DDIR') VOLUMES(VSAMnn) REUSE)
  INDEX(NAME('userid.DDIR.I') TRACKS(1 1) )
  DATA(NAME('userid.DDIR.D') CYLINDERS(1 1) KEYS(128 0)
    RECORDSIZE(384 3072) )

IPCSDDIR 'userid.DDIR'
ALLOCATE DDNAME(IPCSDDIR) DSNAME('userid.DDIR') SHR
ALTLIB ACTIVATE APPLICATION(CLIST) DA('SYS1.SBLSCLI0')

After doing all this, you can now EX the IPCS panel using this TSO command:
EX 'SYS1.SBLSCLI0(BLSCLIBD)'

-----------------------------------------------------

VM:
https://www.ibm.com/docs/en/zvm/7.2?topic=osas-removing-osa-from-system


----------------------------------------------------

AF OPER

Afs  -start
Afc -cycle
Afp -stop

----------------------------------------------------

Check Unix SS Path:
echo $PATH

hostname -g
pasearch -t
curl 
Java -version

find / -name known_hosts
https://www.ibm.com/docs/en/aix/7.1?topic=files-finding-find-command

_BPX_JOBNAME='SSHD' /usr/sbin/sshd

ls -al 
 sudo apt update. - update your libraries
 sudo apt install finger
 finger userid. - inspects another user

 grep.  - it is used after a pipe |. So like
 ip address | grep eth0
 awk - also after pipe
 ip address | grep eth0 | awk ’{print $2}’
 resolvectl status. - resolver info

pasearch -t | grep 'policyRule'

 ping 
-c (count how many pings) 
-s (size of the packet

 whois
 whoami
 whatis. - gives some info
 man - manual command
 which. - will tell you where the program is (one place)
 whereis - will tell you all places the program is
 uname -a   -os information
 df -H.   - disk space
 ps -aux.   -will give you all running processes 
 kill -9 psid.   - -9 is force
 pkill -f processname
 
  cat. -reads the whole thing
 less - read page by page (much better)
 head - read only beginning
  tail - read only end
 cmp - compares 2 files and tells you if it has differences
 diff - compares 2 files and will tell you what the difference is
 sort - sorts in alphabetical order
 find / -name “”. - it is find then in which directory then the name of the file

Find hidden files:
 find . -type f -name “.”

Find empty directories:
 find . -type f -empty

Find executables
 find . -perm /a=x  
 
 netstat tulpn
 
  cat file | sort.   - using | or pipe command lets you add to the command

 ssh-keygen -A.  - will create a set of hosts keys
 ssh-keygen -f “home/.ssh/known_hosts” -R  hostname.   - will remove that host key

 rm. Remove file
 rm -r directory. - using the -r for recursive it deletes directories that are not empty 
 rmdir remove dir
 rm filename.* / or filen* will delete filen+anycharacter, like rm ssh_host_*
 mkdir
 cp
 cp -r . /newdir.  - will copy all files including hidden ones 
 mv move a file - cut
 ln -s filename path.  -this is to link, create a link to a file -s is for soft
 clear

 su userid. - you can access another user credential
 passwd. - change your password
 sudo passwd userid. - change someone elses pass

 touch filename{1…10}    -will create 10 files called filename1 to 10
 touch -d tomorrow filename.  -the -d means it will specify the date of creation

 echo “something” > file.   -this will add the text into that file

 vim
 I to start inserting text
 Esc to stop
 ;wq to write quit

curl http > filename.   - downloads to a file

Create bash for sftp:

 mkdir /u/users/$userid
 chgmod 755 /u/users/$userid
 chgown $userid /u/users/$userid
 mkdir /u/users/$userid/.ssh
 chgmod 755 /u/users/$userid/.ssh
 chgown $userid /u/users/$userid/.ssh
 ssh-keygen -t rsa -f /u/users/$userid/.ssh/
 chgown $userid /u/users/$userid/.ssh/id_rsa
 cp -r /u/users/otheruser/. /u/users/$userid

Create bash for checking policies:

 cat /etc/pagent/pagent_TTLS.conf
 pasearch -t

Create bash for checking directories:

 cd /tmp/
 cd /etc/

Just take it from BPXPRMxx

Cmd1; cmd2  - run next command

Cmd1 && cmd2 - run next only if successful 

Cmd1 || cmd2 - run next only if fail



----------------------------------------------------


JES2 Commands:
$P LINE(2-*)
$S LINE(40)
https://www.ibm.com/docs/en/zos/2.3.0?topic=section-p-linennnnn-stop-line
$DPROC 

$SUBMIT
https://www.ibm.com/docs/en/zos/2.4.0?topic=section-submit-submit-member-from-submitlib

----------------------------------------------------

SSL JAVA
https://www.ibm.com/docs/en/db2/9.7?topic=ssl-configuring-java-runtime-environment-use
https://www.ibm.com/docs/en/db2/11.1?topic=ssl-configuring-java-runtime-environment-use
https://www.ibm.com/docs/pt/sim/6.0.0.22?topic=middleware-configuring-ssl-websphere-application-server
https://www.ibm.com/docs/en/cics-ts/5.3?topic=sja-configuring-ssl-tls-liberty-jvm-server-using-java-keystore
https://www.ibm.com/docs/en/db2/11.5?topic=ssl-configuring-java-runtime-environment-use
https://www.ibm.com/docs/en/db2/10.1.0?topic=ssl-configuring-java-runtime-environment-use

---------------------------------------------------

SETPROG APF,ADD,DSN=load.new ,VOLUME= newvol

----------------------------------------------------


Windows:

 ipconfig /all
 Find string on any command: ipconfig /all | findstr dns
 ipconfig /release - /renew
 ipconfig /displaydns
 | clip - copies output to clipboard
 ipconfig /displaydns | clip
 ipconfig /flushdns
 nslookup hostname dnsserverip
 nslookup -type=txt hostname
Type:
 mx - mail
 ptr - pointer
 txt - text

 assoc - will tell you which files are associated to which program 
 assoc .mp4=VLC.vlc

 cls - clean screen
 getmac /v

 powercfg /energy - /batteryreport
 chkdsk /f (fix) /r (physical sector issues)  
 sfc /scannow
 DISM /Online /Cleanup-image /CheckHealth
 Basic
Deeper - /ScanHealth
Deeper - /RestoreHealth
Do sfc /scannow afterwards

 tasklist | findstr script
 taskkill /f /pid pid

 netsh wlan show wlanreport
 netsh interface ip show address
 netsh interface ip show dnsservers
 netsh advfirewall set allprofiles status off

 ping:
 -t infinite ping

 tracert:
 -d will not resolve host names

 netstat:
 -af
 -o
 -e -t 5

 route:
 print
 add network mask interface
  add 192.168.4.0 mask 255.255.255.0 192.168.1.10
 delete 192.168.4.0

Restart to BIOS
 shutdown /r /fw /f  /t 0
 

