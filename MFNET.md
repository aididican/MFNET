# MFNET UTILS

## Purpose of this document

This document is meant to be a reference guide for zOS practicioners. Oriented mostly to Communications Server configuration, troubleshooting and related applications.

-----------------------------------------

# INDEX

## Communication Server Commands

[VTAM](#vtam)

[VTAM Display Commands](#display)

[VTAM Vary Commands](#vary)

[VTAM Trace](#trace)

[Enterprise Extender](#ee)

[OMVS Commands](#omvs)

[JES Commands](#jes)

[TPX](#tpx)

[TCPIP](#tcpip)

[TN3270](#tn3270)

[TCPIP Troubleshoot](#troubleshoot)

[RESOLVER](#resolver)

[MAKESITE](#makesite)

[OMPROUTE](#omproute)

[SNMP](#snmp)

[ATTLS](#attls)

[GSKKYMAN](#gskkyman)

[CSF](#csf)

[CONSOLES](#consoles)

[CTTRACE](#cttrace)

[ESF Printers](#esf-printers)

[NPF Printers](#npf-printers)

[JES Printers](#jes-printers)

[VPS](#vps)

[SMF](#smf)

## Useful Commands (NOT Communications Server)

[Useful](#useful)

## File Transfer

[XMIT](#xmit)

[Connect Direct](#connect-direct)

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

[INDEX](#index)
-------------------------------------------------------

## VTAM


S NET,,,(LIST=&VTAMSYMB)
START-- --procname--,--,--,--(--| Options |--)--------------><

https://www.ibm.com/docs/en/zos/2.2.0?topic=commands-start-command

https://www.ibm.com/docs/en/zos/2.1.0?topic=profile-conntype-statement
-CONNTYPE--+-SECURE-----+-'   
               +-NEGTSECURE-+     
               +-BASIC------+     
               +-ANY--------+     
               '-NONE-------' 

ATCSTR Options:

https://www.ibm.com/docs/en/zos/2.3.0?topic=commands-start-options

[INDEX](#index)
--------------------------------------------------------

## Display

D NET,STATIONS
D NET,SESSIONS,SCOPE=ALL,LIST=ALL
D NET,MAJNODES
D NET,VTAMOPTS
D NET,BFRUSE,BUFFER=SHORT
D NET,CSM,OWNERID=ALL
D NET,EE,LIST=DETAIL
D NET,TGPS
D NET,TRL

D NET,TABLE,ID=TABLE,E
https://www.ibm.com/docs/en/zos/2.3.0?topic=commands-display-table-command


RTP Connection
https://www.ibm.com/docs/en/zos/2.1.0?topic=determination-display-id-rtp-connection

Sessions
https://www.ibm.com/docs/en/zos/2.4.0?topic=commands-display-sessions-command

D NET,SESSION,SID=
D NET,E,ID=RTPSESS

D NET,APPLS,SCOPE=ACTSESS
https://www.ibm.com/docs/en/zos/2.3.0?topic=commands-display-appls-command

D NET:
https://www.ibm.com/docs/en/zos/2.3.0?topic=commands-display-id-command

D NET,ID=xxx,SCOPE=CONCT


APING 
https://www.ibm.com/docs/en/zos/2.3.0?topic=commands-display-aping-command
https://www.ibm.com/docs/en/zos/2.3.0?topic=commands-display-apingdtp-command
https://www.ibm.com/docs/en/zos/2.3.0?topic=commands-display-apingtp-command

APPLS 
https://www.ibm.com/docs/en/zos/2.3.0?topic=commands-display-appls-command
https://www.ibm.com/docs/en/zos/2.3.0?topic=commands-display-appntosa-command


AUTOLOG 
https://www.ibm.com/docs/en/zos/2.3.0?topic=commands-display-autolog-command

BFRUSE 
https://www.ibm.com/docs/en/zos/2.3.0?topic=commands-display-bfruse-command

BNCOSMAP
https://www.ibm.com/docs/en/zos/2.3.0?topic=commands-display-bncosmap-command



ADJCLUST
https://www.ibm.com/docs/en/zos/2.3.0?topic=commands-display-adjclust-command
https://www.ibm.com/docs/en/zos/2.3.0?topic=commands-display-adjcp-command
https://www.ibm.com/docs/en/zos/2.3.0?topic=commands-display-adjsscps-command

https://www.ibm.com/docs/en/zos/2.1.0?topic=commands-using-vtam-display-problem-determination

https://www.ibm.com/docs/en/zos/2.4.0?topic=commands-display-aping-command

https://www.ibm.com/docs/en/zos/2.3.0?topic=commands-display-id-command

https://www.ibm.com/docs/en/zos/2.4.0?topic=commands-display-vtamopts-command

https://www.ibm.com/docs/en/zos/2.4.0?topic=commands-display-tgps-command

https://www.ibm.com/docs/en/zos/2.3.0?topic=commands-display-appls-command

https://www.ibm.com/docs/en/zos/2.1.0?topic=commands-display-terms-command

https://www.ibm.com/docs/en/zos/2.2.0?topic=commands-display-table-command

https://www.ibm.com/docs/en/zos/2.4.0?topic=commands-display-majnodes-command

https://www.ibm.com/docs/en/zos/2.1.0?topic=section-d-network-display-network-activity

https://www.ibm.com/docs/en/zos/2.1.0?topic=commands-display-eediag-command

https://www.ibm.com/docs/en/zos/2.3.0?topic=commands-display-directry-command

https://www.ibm.com/docs/en/zos/2.3.0?topic=commands-display-adjclust-command

https://www.ibm.com/docs/en/zos/2.1.0?topic=commands-display-topo-command

https://www.ibm.com/docs/en/zos/2.3.0?topic=commands-display-csm-command

https://www.ibm.com/docs/en/zos/2.2.0?topic=commands-display-trl-command

https://www.ibm.com/docs/en/zos/2.4.0?topic=commands-d-stations-command

https://www.ibm.com/docs/en/zos/2.3.0?topic=commands-display-netsrvr-command

https://www.ibm.com/docs/en/zos/2.4.0?topic=commands-display-bfruse-command

https://www.ibm.com/docs/en/zos/2.4.0?topic=commands-display-cpcp-command

https://www.ibm.com/docs/en/zos/2.4.0?topic=commands-display-csdump-command

https://www.ibm.com/docs/en/zos/2.4.0?topic=commands-display-sessions-command

[INDEX](#index)
------------------------------------------------------------------------

## Vary

Kill SNA SESSION
https://www.ibm.com/docs/en/zos/2.1.0?topic=commands-vary-term-command
V NET,TERM,SID=,TYPE=FORCE


Update same table
F NET,TABLE,TYPE=MODETAB,OPTION=LOAD,NEWTAB=IDB2TBL

Update with new table
F NET,TABLE,TYPE=MODETAB,OPTION=LOAD,NEWTAB=new,OLDTAB=old
https://www.ibm.com/docs/en/zos/2.2.0?topic=commands-modify-table-command
https://docs.bmc.com/docs/mcdv630/defining-a-default-vtam-mode-table-entry-856647506.html
https://www.ibm.com/docs/en/zos/2.2.0?topic=commands-modify-table-command

MODETAB
https://www.ibm.com/docs/en/zos/2.1.0?topic=interface-logon-mode-table
https://www.ibm.com/docs/en/zos/2.3.0?topic=udtdf-logon-mode-table
https://www.ibm.com/docs/en/zos/2.3.0?topic=table-logon-mode-full-syntax
https://www.ibm.com/docs/en/zos/2.1.0?topic=tasks-defining-appcmvs-logon-mode-entry-in-vtamlib


MODIFY defaults
https://www.ibm.com/docs/en/zos/2.2.0?topic=commands-modify-defaults-command#fde


https://www.ibm.com/docs/en/zos/2.4.0?topic=commands-vary-inact-command

https://www.ibm.com/docs/en/zos/2.4.0?topic=commands-vary-act-command

https://www.ibm.com/docs/en/zos/2.4.0?topic=commands-modify-trace-command

https://www.ibm.com/docs/en/zos/2.4.0?topic=commands-modify-csdump-command

[INDEX](#index)
--------------------------------------------------------------------------

## TRACE


Start VTAM internal trace on both sides:  
F NET,trace,type=vtam,size=200m,opt=(CIO,PIU,CIA,MSG,PSS)
Start GTF CCW trace with options:

S GTF,,,(MODE=EXT)

*6913 AHL125A  RESPECIFY TRACE OPTIONS OR REPLY U
  TRACE=IOP,SSCHP,CCWP

*6915 AHL101A  SPECIFY TRACE EVENT KEYWORDS --IO=,SSCH=,CCW=,IO=SSCH=
R 6915,IO=SSCH=4112

*6932 AHL102A  CONTINUE TRACE DEFINITION OR REPLY END 
R 6932,CCW=(SI,CCWN=50,DATA=2048,IOSB)

R 6933,END                                       
IEE600I REPLY TO 6933 IS;END                     
END                                              
AHL103I  TRACE OPTIONS SELECTED --,IO=SSCH=(4112)
AHL103I  CCW=(SI,IOSB,CCWN=50,DATA=2048)         
*6934 AHL125A  RESPECIFY TRACE OPTIONS OR REPLY U 

AHL031I GTF INITIALIZATION COMPLETE 
  IO=SSCH=4112        
 CCW=(SI,CCWN=50,DATA=2048,IOSB) 
Recreate the problem. When the problem state occurs,  dump both VTAMs using F NET,CSDUMP and stop VIT and GTF.
To stop GTF: STOP GTF
To stop VIT: F NET,NOTRACE,TYPE=VTAM,MODE=INT,OPTION=END
Action Plan: Await doc or results of change to MIHTMOUT.


D IOS,MIH,DEV=4112

https://www.ibm.com/docs/en/zos/2.3.0?topic=gtf-starting-trace-vtam-remote-network-activity
https://www.ibm.com/docs/en/zos/2.2.0?topic=communication-specifying-gtf-trace-options
https://www.ibm.com/docs/en/zos/2.2.0?topic=sg-specifying-changing-gtf-trace-options-through-system-prompting
https://www.ibm.com/docs/en/zos/2.4.0?topic=gtf-stopping
https://www.ibm.com/docs/en/zos/2.4.0?topic=command-displaying-mih-io-timing-limits-iosmih
https://www.ibm.com/docs/en/ts7700-virtual-tape/4.2?topic=STFS69_4.2.0/ts7700_setting_mih.htm

[INDEX](#index)
-------------------------------------------------------------------------

## EE


XCF and EE 
https://www.ibm.com/docs/en/zos/2.4.0?topic=distributor-route-selection-distributing-packets
https://www.ibm.com/docs/en/zos/2.4.0?topic=ecaxmn-external-communication-adapter-xca-major-node-operand-descriptions

[INDEX](#index)
--------------------------------------------------------------------------

## OMVS

D OMVS,O

D OMVS,P

D OMVS,L

STOP OMVS processes from JES2:
D OMVS,A=ALL

From <https://www.ibm.com/docs/en/zos/2.4.0?topic=psufo-steps-shutting-down-zos-unix-using-f-omvsshutdown> 

F OMVS,STOPPFS=NFS - HFS or ZFS

From <https://www.ibm.com/docs/en/zos/2.4.0?topic=psufo-steps-shutting-down-zos-unix-using-f-omvsshutdown> 


F BPXOINIT,SHUTDOWN=FORKINIT - stops OMVS stuff like BPXAS

F OMVS,RESTART

F OMVS,SHUTDOWN

[INDEX](#index)
--------------------------------------------------------

## JES

$djes2 - displays anything running on JES2

JES NODE - NJE

$D NODE
$D LINE 
$SN,N=nodename
$S N,LINEx,SOCKET=nodename

$pjes2 - stops JES2

[INDEX](#index)
----------------------------------------------------------

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

RELOAD

https://techdocs.broadcom.com/us/en/ca-mainframe-software/traditional-management/ca-tpx-session-management/5-4/operating/operator-commands/reload-command.html

RELOAD PROF=
RELOAD TABLE=
RELOAD ACT=
RELOAD SMRT=smrtname
D U,SUMM
S TPX,SMRT=smrtname

[INDEX](#index)
-----------------------------------------

## TCPIP


STOP TCPIP
/FORCE TCPIP,ARM


D TCPIP,,N,CONFIG
D TCPIP,,N,HOME
D TCPIP,,N,STATS
D TCPIP,,N,ROUTE,MAX=*
D TCPIP,,OMPROUTE,OSPF,LIST,ALL
D TCPIP,,OMPROUTE,RIP,LIST,ALL

TCPIP PROFILE CONFIG:
https://www.ibm.com/docs/en/zos/2.2.0?topic=statements-tcpconfig-statement

SACONFIG ENABLED COMMUNITY public AGENT 161

TCPIP PROFILE DELETE:
https://www.ibm.com/docs/en/zos/2.1.0?topic=statements-delete-statement
https://www.ibm.com/docs/en/zos/2.1.0?topic=messages-ezz0395i

D TCPIP,,N,CONN,CONNT=TTLSP

D TCPIP,,N,CONN,SERVER -- ONLY LISTEN STATUS

https://www.ibm.com/docs/en/zos/2.2.0?topic=commands-display-topo-command

DEBUG
https://www.ibm.com/docs/en/zos/2.1.0?topic=messages-ezz6035i

Interfaces
https://www.ibm.com/docs/en/zos/2.2.0?topic=statements-interface-ipaqenet-osa-express-qdio-interfaces-statement
https://www.ibm.com/docs/en/zos/2.3.0?topic=statements-summary-interface#interf
https://www.ibm.com/docs/en/zos/2.3.0?topic=statements-summary-device-link
https://www.ibm.com/docs/en/zos/2.2.0?topic=statements-monitoring-network-interfaces-interface
https://www.ibm.com/docs/en/zos/2.3.0?topic=vlan-configuration-recommendations
https://www.ibm.com/docs/en/zos/2.4.0?topic=cnha-steps-converting-from-ipv4-ipaqenet-device-link-home-definitions-ipv4-ipaqenet-interface-statement

DEVICE and LINK:
https://www.ibm.com/docs/en/zos/2.2.0?topic=tppcs-device-link-mpcipa-osa-express-qdio-devices-statement
https://www.ibm.com/docs/en/zos/2.2.0?topic=statements-steps-modifying-device-link


DROP 
https://www.ibm.com/docs/en/zos/2.4.0?topic=space-vary-tcpipdrop
Vary 
TCPIP
,
procname
,
DRop,
CMD=DRop,
connid
CONNection=
connid

[INDEX](#index)
----------------------------------------------------------

## TN3270

TN3270
https://www.ibm.com/docs/en/zos/2.4.0?topic=telnet-commands
https://www.ibm.com/docs/en/zos/2.4.0?topic=space-vary-tcpiptnproctelnet
https://www.ibm.com/docs/en/zos/2.4.0?topic=SSLTBW_2.4.0/com.ibm.zos.v2r4.halu101/varystopcmd.html
https://www.ibm.com/docs/en/zos/2.4.0?topic=server-managing-telnet
V TCPIP,TN3270,O,DSN=XXX
V TCPIP,TN3270,STOP,PORT=23
D TCPIP,TN3270,PROFILE


TN3270
https://www.ibm.com/docs/en/zos/2.3.0?topic=command-display-tn3270e-telnet-server-address-space
https://www.ibm.com/docs/en/zos/2.3.0?topic=space-display-telnet-connection-command#dtel
https://www.ibm.com/docs/en/zos/2.3.0?topic=commands-display-tcpip-telnet
https://www.ibm.com/docs/en/zos/2.4.0?topic=space-display-telnet-profile-command
https://www.ibm.com/docs/en/zos/2.1.0?topic=files-tn3270e-telnet-server-profile-configuration-file
https://www.ibm.com/docs/en/zos/2.1.0?topic=server-telnet-profile-statements-overview
https://www.ibm.com/docs/en/zos/2.1.0?topic=server-telnet-parameter-statements-in-telnet-profile
Display TCPIP
,tnproc
,Telnet
,CLientID
,OBJect
,PROFile
,CONNection
,INACTLUS

PORT and PARM Definitions
https://www.ibm.com/docs/en/zos/2.1.0?topic=security-transport-layer


LU NAMES
https://www.ibm.com/docs/en/zos/2.1.0?topic=profile-rules-lu-name-specification

https://www.ibm.com/docs/en/zos/2.1.0?topic=server-telnet-parameter-statements-in-telnet-profile
https://www.ibm.com/docs/en/zos/2.1.0?topic=profile-rules-telnet-parameter-statements-security-parameters#vtamrul
https://www.ibm.com/docs/en/zos/2.4.0?topic=ttss-secure-non-secure-connections-using-single-telnet-port
https://www.ibm.com/docs/en/zos/2.4.0?topic=ssl-tn3270e-telnet-server-security
https://www.ibm.com/docs/en/zos/2.2.0?topic=profile-keyring-statement
https://www.ibm.com/docs/en/zos/2.4.0?topic=ttss-secure-non-secure-connections-using-single-telnet-port#security_tn3270e_mixed_traffic__secsing

SMF Records

https://www.ibm.com/docs/en/zos/2.1.0?topic=profile-smfinit-smfterm-statements

[INDEX](#index)
------------------------------------------------

## Troubleshoot

https://www.ibm.com/docs/en/zos/2.4.0?topic=server-zos-communications-ip-diagnosis-guide
https://www.ibm.com/docs/en/zos/2.3.0?topic=space-display-telnet-connection-command#dtel
https://www.ibm.com/docs/en/zos/2.3.0?topic=commands-display-tcpip-telnet


------------------------------------------------

NETSTAT

NETSTAT
https://www.ibm.com/docs/en/zos/2.3.0?topic=commands-display-tcpip-netstat
DISPLAY TCPIP NETSTAT

D TCPIP,,N,CONN,
                CLIENT=
				PORT=
				SERVER
				MAX=*
		        CONNT=TTLSP	
				
---------------------------------------------------

TRACERTE
https://www.ibm.com/docs/en/zos/2.4.0?topic=traceroute-tso-tracerte-command-debug-network-problems

				
---------------------------------------------------

NSLOOKUP UNIX

https://www.ibm.com/docs/en/zos/2.3.0?topic=command-nslookup-examples
https://www.ibm.com/docs/en/zos/2.3.0?topic=command-nslookup-query-name-server-in-mode
https://www.ibm.com/docs/en/zos/2.3.0?topic=command-nslookup-options#optdns
https://www.ibm.com/docs/en/zos/2.3.0?topic=utnc-nslookup-configuration
https://www.ibm.com/docs/en/zos/2.3.0?topic=utnc-nslookup-issue-queries-name-servers-in-interactive-mode
https://www.ibm.com/docs/en/zos/2.3.0?topic=command-nslookup-options



---------------------------------------------------

PING 
https://www.ibm.com/docs/en/zos/2.1.0?topic=network-ping

https://www.ibm.com/docs/en/zos/2.4.0?topic=ping-tso-command-send-echo-request

ping 8.8.8.8 (intf intfname


PING UNIX 
https://www.ibm.com/docs/en/zos/2.2.0?topic=ping-zos-unix-command-send-echo-request
https://www.ibm.com/docs/en/zos/2.2.0?topic=ping-tso-command-send-echo-request
Format
Read syntax diagramSkip visual syntax diagram
>>-ping--+-+------------+-- host_name-+------------------------><
         | '-| Option |-'             |   
         +- -h------------------------+   
         '- -?------------------------'   

Option

   .---------------------.   
   V                     |   
|----+-----------------+-+--------------------------------------|
     +- -A-+-ipv4-+----+     
     |     '-ipv6-'    |     
     |     .-1----.    |     
     +- -c-+------+----+     
     |     '-echo-'    |     
     +- -i interface---+     
     |     .-256---.   |     
     +- -l-+-------+---+     
     |     '-bytes-'   |     
     +- -n-------------+     
     +- -P-+-yes----+--+     
     |     '-ignore-'  |     
     +- -p tcpname-----+     
     +- -s srcip-------+     
     |     .-10------. |     
     +- -t-+---------+-+     
     |     '-seconds-' |     
     '- -v-------------'     

[INDEX](#index)
----------------------------------------------------------

## RESOLVER


F RESOLVER,DISPLAY
F RESOLVER,REFRESH
F RESOLVER,FLUSH,ALL

https://www.ibm.com/docs/en/zos/2.4.0?topic=command-modify-resolver-address-space
https://www.ibm.com/docs/en/zos-basic-skills?topic=information-resolver-address-space
https://www.ibm.com/docs/en/zos-basic-skills?topic=information-type-application-mvs-zos-unix
https://www.ibm.com/docs/en/zos/2.2.0?topic=environment-base-resolver-configuration-files
GLOBALTCPIPDATA
This statement is used to identify a specific resolver configuration file that contains the resolver configuration statements (NAMESERVER, HOSTNAME, and so on) that are to be applied globally to all IP applications.
DEFAULTTCPIPDATA
This statement is used to define a default resolver configuration file that is used as a last resort.
https://www.ibm.com/docs/en/zos/2.3.0?topic=customization-configuring-profiletcpip


The search order used to access the base resolver configuration file is as follows:

GLOBALTCPIPDATA
If defined, the resolver GLOBALTCPIPDATA setup statement value is used. For a description of the GLOBALTCPIPDATA statement, see The resolver and the global TCPIP.DATA file.

The search continues for an additional configuration file. The search ends with the next file found.

The value of the environment variable RESOLVER_CONFIG
The value of the environment variable is used. This search will fail if the file does not exist or is allocated exclusively elsewhere.

/etc/resolv.conf
//SYSTCPD DD card
The data set allocated to the ddname SYSTCPD is used. In the z/OS® UNIX environment, a child process does not have access to the SYSTCPD DD. This is because the SYSTCPD allocation is not inherited from the parent process over the fork() or exec function calls.

userid.TCPIP.DATA
userid is the user ID that is associated with the current security environment (address space or task/thread)

SYS1.TCPPARMS(TCPDATA)
DEFAULTTCPIPDATA
If defined, the resolver DEFAULTTCPIPDATA setup statement value is used. For a description of the DEFAULTTCPIPDATA statement, see The resolver and the global TCPIP.DATA file.

TCPIP.TCPIP.DATA

https://www.ibm.com/docs/en/aix/7.2?topic=resolution-name
https://www.ibm.com/docs/en/aix/7.2?topic=resolution-local-name-etchosts-tasks
https://www.ibm.com/docs/en/aix/7.2?topic=resolution-configuring-host-use-name-server
List All the Hosts	smit lshostent	Use the hostent command or view /etc/hosts
Add a Host	smit mkhostent	Use the hostent command or edit /etc/hosts
Change/Show Characteristics of a Host	smit chhostent	Use the hostent command or edit /etc/hosts
Remove a Host	smit rmhostent	Use the hostent command or edit /etc/hosts

TCPIP.DATA:
https://www.ibm.com/docs/en/zos/2.2.0?topic=stack-tcpipdata-search-order
https://www.ibm.com/docs/en/zos/2.2.0?topic=files-search-orders-used-in-zos-unix-environment#unixso
RESOLVER SEARCH ORDER
https://www.ibm.com/docs/en/zos/2.2.0?topic=resolver-configuration-files#resconf__ftypet

RESOLVER SETUP FILE:

DEFAULTTCPIPDATA('HLQ.Q(MEMBER)')
GLOBALTCPIPDATA('HLQ.Q(MEMBER)')
NOCOMMONSEARCH
CACHE
NOCACHEREORDER
CACHESIZE(200M)
MAXTTL(2147483647)
MAXNEGTTL(2147483647)
UNRESPONSIVETHRESHOLD(25)

[INDEX](#index)
--------------------------------------------------------------------

## MAKESITE


HOSTS FILE
MAKESITE
MAKESITE HLQ=TCPIP,VOLSER=volser,UNIT=SYSDA
https://www.ibm.com/docs/en/zos/2.1.0?topic=commands-makesite-command
Format
Read syntax diagramSkip visual syntax diagram
>>-MAKESITE--+-----------+--,----------------------------------->
             '-HLQ=--hlq-'      

>--+-----------------------------+--,--------------------------->
   '-MGMTclas=--management_class-'      

>--+-----------------------+--,--+--------------------------+--->
   '-DATAclas=--data_class-'     '-STORclas=--storage_class-'   

>--,--+-------------+--,--+------------------------+-----------><
      '-Unit=--unit-'     '-VOLser=--volume_serial-'  

https://www.ibm.com/docs/en/zos-basic-skills?topic=information-search-order-resolver-configuration
//SYSTCPD DD card. The data set allocated to the DDname SYSTCPD is used. In the z/OS UNIX environment, a child process does not have access to the SYSTCPD DD. This is because the SYSTCPD allocation is not inherited from the parent process over the fork() or exec function calls.
userid.TCPIP.DATA. "userid" is the user ID that is associated with the current security environment (address space or task/thread). An MVS environment application could theoretically run without an associated user ID. If so, the job name would be used for this data set instead.
SYS1.TCPPARMS(TCPDATA)
DEFAULTTCPIPDATA. If defined, the resolver DEFAULTTCPIPDATA setup statement value is used.
TCPIP.TCPIP.DATA

As a batch job, you might use this JCL:
//MAKESITE JOB ,TIME=2,NOTIFY=USER7
//*
//BATCH  EXEC PGM=MAKESITE,REGION=8000K,
//  PARM='VOLSER=volser,UNIT=SYSDA,HLQ=TCPIP,'
//*
//STEPLIB DD DISP=SHR,DSN=TCPIP.SEZALOAD
//SYSPRINT  DD  SYSOUT=*,DCB=(LRECL=132,RECFM=FBA,BLKSIZE=3960)
//SYSABEND  DD  SYSOUT=*
//

[INDEX](#index)
----------------------------------------------------------------

## OMPROUTE

OMPROUTE
https://www.ibm.com/docs/en/zos/2.4.0?topic=routing-steps-configuring-ospf-rip-ipv4-ipv6
https://manualzz.com/doc/28975554/z-os-omproute-hints-and-tips
https://www.ibm.com/docs/en/zos/2.3.0?topic=statements-ospf-configuration
https://www.ibm.com/docs/en/ssw_ibm_i_73/pdf/rzal6ospfpdf.pdf
https://www.ibm.com/docs/en/zvm/7.1?topic=ospf-default-route

D TCPIP,,OMPROUTE,OSPF,LIST,ALL
D TCPIP,,OMPROUTE,RIP,LIST,ALL

[INDEX](#index)
-----------------------------------------------------

## SNMP

 
SNMP

snmp -c communityname walk system

Snmp -c comm -h host -a (use interfaces) -v (verbose) -d 4 (0-4 values) 

Snmp command:
https://www.ibm.com/docs/en/zos/2.4.0?topic=snmp-zos-unix-command

https://www.ibm.com/docs/en/zos/2.2.0?topic=osnmpd-parameters
SACONFIG ENABLED COMMUNITY public AGENT 161
https://www.ibm.com/docs/en/zos/2.2.0?topic=statements-saconfig-statement

Configuration:

https://www.ibm.com/docs/en/zos/2.2.0?topic=osnmpd-parameters
https://www.ibm.com/docs/en/zos/2.2.0?topic=needs-community-based-security
https://www.ibm.com/docs/en/zos/2.2.0?topic=dssn-decide-your-security-needs-community-based-user-based
https://www.ibm.com/docs/en/zos/2.2.0?topic=information-creating-user-keys#pwtok1
https://www.ibm.com/docs/en/zos/2.2.0?topic=overview-snmp-agent
https://www.ibm.com/docs/en/zos/2.2.0?topic=file-steps-migrating-pwsrc-snmptrapdest-files
https://www.ibm.com/docs/en/zos/2.2.0?topic=agent-provide-tcpip-profile-statements
https://www.ibm.com/docs/en/zos/2.2.0?topic=information-pwsrc-example
https://www.ibm.com/docs/en/zos/2.2.0?topic=agent-sample-jcl-procedure-starting-osnmpd-from-mvs
https://www.ibm.com/docs/en/zos/2.2.0?topic=agent-starting-osnmpd-from-zos-unix
https://www.ibm.com/docs/en/zos/2.2.0?topic=subagents-connecting-agent-through-tcp
https://www.ibm.com/docs/en/zos/2.2.0?topic=agent-allowing-subagents-duplicate-identifiers-connect
https://www.ibm.com/docs/en/zos/2.2.0?topic=agent-provide-mib-object-configuration-information
https://www.ibm.com/docs/en/zos/2.2.0?topic=agent-common-inet-considerations
https://www.ibm.com/docs/en/zos/2.2.0?topic=agent-start-snmp

SACONFIG ENABLED COMMUNITY public AGENT 161


[INDEX](#index)
---------------------------------------------------

## ATTLS


ATTLS

pasearch Command
https://www.ibm.com/docs/en/zos/2.1.0?topic=information-zos-unix-pasearch-command-display-policies

Implement TLS 1.2 without ATTLS:
https://www.ibm.com/support/pages/zos-communications-server-tls-needed-implement-tls-v12

Guide:
https://www.ibm.com/docs/en/zos/2.2.0?topic=security-transport-layer
https://www.ibm.com/docs/en/rtw/9.0.1?topic=clip-setting-up-tls#ritzos_attls__attls5

Setting Up RACF Permits for Stack Access (EZZ4248E TCPIP waiting for PAGENT):
https://www.ibm.com/support/pages/during-tls-startup-message-ezz4248e-written-console-not-released

For Clients:
https://www.ibm.com/docs/en/zos/2.2.0?topic=tls-configuring-client-systems

For Servers:
https://www.ibm.com/docs/en/zos/2.2.0?topic=tls-configuring-server-system

For TN3270:
https://www.ibm.com/support/pages/system/files/inline-files/An_Introduction_to_AT-TLS_for_FTP_and_TN3270.pdf

PARAMETERS
https://www.ibm.com/docs/en/zos/2.4.0?topic=applications-tls-policy-statements#tlspol

TLS 1.3
https://www.ibm.com/docs/en/zos/2.4.0?topic=security-tls-support-tls-v13

https://www.ibm.com/docs/en/rtw/9.0.1?topic=clip-setting-up-tls#ritzos_attls__attls5
https://www.ibm.com/support/pages/system/files/inline-files/An_Introduction_to_AT-TLS_for_FTP_and_TN3270.pdf
https://www.ibm.com/support/pages/zos-communications-server-tls-needed-implement-tls-v12
https://www.ibm.com/docs/en/integration-bus/10.0?topic=tls-configuring-activating-policy-agent-pagent
https://www.ibm.com/docs/en/zos/2.4.0?topic=statements-ttlsenvironmentadvancedparms-statement
https://www.ibm.com/docs/en/zos/2.2.0?topic=security-transport-layer
https://www.ibm.com/docs/en/integration-bus/10.0?topic=tls-configuring-activating-policy-agent-pagent
https://www.ibm.com/docs/en/ibm-mq/9.1?topic=codes-transport-layer-security-tls-return-zos
https://www.ibm.com/docs/es/rtw/9.0.1?topic=clip-setting-up-tls
https://www.ibm.com/docs/en/zos/2.2.0?topic=statements-tcpconfig-statement
     | '-TIMEWAITInterval seconds-'                        |     
     | .-NOTTLS-.                                          |     
     '-+--------+------------------------------------------'     
       '-TTLS---'      
	   
https://www.ibm.com/support/pages/how-can-we-determine-whether-tls-connection-mapped-tls-policy
https://www.ibm.com/support/pages/how-can-i-determine-whether-tlsv12-enabled-my-tls-connections


SSL Import
https://www.ibm.com/docs/en/zos/2.1.0?topic=menu-import-certificate
https://www.ibm.com/docs/en/zos/2.1.0?topic=menu-import-certificate-private-key
https://www.ibm.com/docs/en/zos/2.1.0?topic=03353xxx-0335301f
https://www.ibm.com/docs/en/zos/2.3.0?topic=sfrc-417
https://marc.info/?l=racf-l&m=151984184415528&w=2


https://techdocs.broadcom.com/us/en/ca-mainframe-software/security/ca-acf2-for-z-os/16-0/administrating/digital-certificate-support/process-digital-certificates-with-ca-acf2.html
https://www.ibm.com/docs/en/zos/2.1.0?topic=gime-importing-certificate-from-file-as-trusted-ca-certificate
https://www.ibm.com/docs/en/zos/2.4.0?topic=certificates-racdcert-add-add-certificate


SSL Troubleshoot

https://www.ibm.com/support/pages/ftp-fails-eza2897i-authentication-negotiation-failed-message
https://access.redhat.com/solutions/548573
https://www.ibm.com/support/pages/why-are-tls-connections-failing-ezd1286i-or-ezd1287i-return-code-428
https://www.ibm.com/docs/en/zos/2.1.0?topic=tls-return-codes
https://www.ibm.com/docs/en/zos/2.4.0?topic=services-zos-cryptographic-system-ssl-programming
https://www.ibm.com/docs/en/zos/2.4.0?topic=codes-ssl-function-return


EZD1281I indicates that the TCP connection with the specified connection ID (CONNID) matched the specified Application Transparent Transport Layer Security (AT-TLS) rule. This CONNID will be used in all future AT-TLS messages for this connection. rule is the name of the TTLSRule that mapped this connection. stat is the AT-TLS status for the connection. The values for stat are:
Not Enabled if TTLSEnabled in the matching AT-TLS policy is set to OFF (AT-TLS security is active. Data might be encrypted, based on other policy statements.).
Enabled if TTLSEnabled in the matching AT-TLS policy is set to ON (AT-TLS security is not active. Data is sent in the clear.).
Appl Control if ApplicationControlled in the matching AT-TLS policy is set to ON (An application can control AT-TLS security. AT-TLS security is used only when requested by the application, using the SIOCTTLSCTL ioctl.).

D TCPIP,,N,CONN,CONNT,TTLSP

ADD TLS Troubleshoot
F PAGENT,REFRESH

LogLevel 511
TLSRFCLEVEL RFC4217

ATTLS TRACE 2 

https://www.ibm.com/docs/en/zos/2.3.0?topic=statements-ttlsconfig-statement
https://www.ibm.com/docs/en/zos/2.5.0?topic=statements-ttlsrule-statement
TTLSConfig  //'USER1.PAGENT.CONF(TTLS)'
TTLSConfig  /u/user1/pagent.ttls

TTLSRule                          PROC
{
  LocalAddr                       ALL
  RemoteAddr                      ALL
  LocalPortRangeRef               portR7
  RemotePortRangeRef              portR2
  Direction                       Inbound
  Priority                        255
  TTLSGroupActionRef              gAct1
  TTLSEnvironmentActionRef        eAct7
  TTLSConnectionActionRef         cAct7
}
TTLSGroupAction                   gAct1
{
  TTLSEnabled                     On
  Trace                           2
}
TTLSEnvironmentAction             eAct7
{
  HandshakeRole                   Server
  Trace                           7
  TTLSKeyringParmsRef             keyR7
  TTLSEnvironmentAdvancedParmsRef eAdv1
}
TTLSEnvironmentAdvancedParms      eAdv1
{
TLSv1.1 On
TLSv1.2 On
ClientAuthType PassThru
}
TTLSConnectionAction              cAct7
{
  HandshakeRole                   Server
  TTLSCipherParmsRef              cipher4~Default_NISTCiphers_z196
  TTLSConnectionAdvancedParmsRef  cAdv7~PROC
  CtraceClearText                 Off
  Trace                           7
}
TTLSConnectionAdvancedParms       cAdv7~PROC
{
  SSLv3                           Off
  TLSv1                           Off
  TLSv1.1                         On
  ApplicationControlled           Off
  SecondaryMap                    Off
  TLSv1.2                         On
  CertificateLabel                PROC_CERT
}
TTLSKeyringParms                  keyR7
{
  Keyring                         PROC_RING
}
PortRange                         portR7
{
  Port                            2470-2471
}
TTLSCipherParms                   cipher5~Default_PROC
{
  V3CipherSuites TLS_DH_DSS_WITH_DES_CBC_SHA
  V3CipherSuites TLS_DH_RSA_WITH_DES_CBC_SHA
  V3CipherSuites TLS_NULL_WITH_NULL_NULL
  V3CipherSuites TLS_RSA_WITH_NULL_MD5
  V3CipherSuites TLS_RSA_WITH_NULL_SHA
  V3CipherSuites TLS_RSA_EXPORT_WITH_RC4_40_MD5
  V3CipherSuites TLS_RSA_EXPORT_WITH_RC2_CBC_40_MD5
  V3CipherSuites TLS_RSA_WITH_DES_CBC_SHA
  V3CipherSuites TLS_DHE_DSS_WITH_DES_CBC_SHA
  V3CipherSuites TLS_DHE_RSA_WITH_DES_CBC_SHA
  V3CipherSuites TLS_RSA_WITH_AES_256_CBC_SHA256
  V3CipherSuites TLS_RSA_WITH_AES_256_CBC_SHA
  V3CipherSuites TLS_ECDHE_ECDSA_WITH_AES_128_CBC_SHA256
  V3CipherSuites TLS_ECDHE_RSA_WITH_AES_128_CBC_SHA256
  V3CipherSuites TLS_RSA_WITH_AES_128_CBC_SHA256
  V3CipherSuites TLS_ECDH_ECDSA_WITH_AES_128_CBC_SHA256
  V3CipherSuites TLS_ECDH_RSA_WITH_AES_128_CBC_SHA256
  V3CipherSuites TLS_DHE_RSA_WITH_AES_128_CBC_SHA256
  V3CipherSuites TLS_DHE_DSS_WITH_AES_128_CBC_SHA256
  V3CipherSuites TLS_ECDHE_ECDSA_WITH_AES_128_CBC_SHA
  V3CipherSuites TLS_ECDHE_RSA_WITH_AES_128_CBC_SHA
  V3CipherSuites TLS_RSA_WITH_AES_128_CBC_SHA
  V3CipherSuites TLS_ECDH_ECDSA_WITH_AES_128_CBC_SHA
  V3CipherSuites TLS_ECDH_RSA_WITH_AES_128_CBC_SHA
  V3CipherSuites TLS_DHE_RSA_WITH_AES_128_CBC_SHA
  V3CipherSuites TLS_DHE_DSS_WITH_AES_128_CBC_SHA
  V3CipherSuites TLS_ECDHE_ECDSA_WITH_AES_128_GCM_SHA256
  V3CipherSuites TLS_ECDHE_RSA_WITH_AES_128_GCM_SHA256
  V3CipherSuites TLS_RSA_WITH_AES_128_GCM_SHA256
  V3CipherSuites TLS_ECDH_ECDSA_WITH_AES_128_GCM_SHA256
  V3CipherSuites TLS_DHE_RSA_WITH_AES_128_GCM_SHA256
  V3CipherSuites TLS_DHE_DSS_WITH_AES_128_GCM_SHA256
  V3CipherSuites TLS_ECDHE_ECDSA_WITH_3DES_EDE_CBC_SHA
  V3CipherSuites TLS_ECDHE_RSA_WITH_3DES_EDE_CBC_SHA
  V3CipherSuites TLS_ECDH_ECDSA_WITH_3DES_EDE_CBC_SHA
  V3CipherSuites TLS_ECDH_RSA_WITH_3DES_EDE_CBC_SHA
}


LASTACK for TLS ISSUES: LE issue

Add to TCPIP PROC
//CEEOPTS  DD *
HEAP64(10M,10M)
HEAPPOOLS64(ON,
24,,48,,72,,136,,192,,272,,
568,,1056,,1584,,3008,,8096,)

[INDEX](#index)
--------------------------------------------

## GSKKYMAN

CLI Commands
https://www.ibm.com/docs/en/zos/2.1.0?topic=syntax-gskkyman-command-line-mode-examples
gskkyman -dc -k filename 

gskkyman
https://www.ibm.com/docs/en/zos/2.1.0?topic=syntax-gskkyman
https://www.ibm.com/docs/en/zos/2.1.0?topic=management-gskkyman-overview


gskkyman -dc|-dcv [-k filename|-t tokenname] [-l label]
gskkyman -dk [-k filename]
gskkyman -e|-i [-k filename|-t tokenname] [-l label] [-p filename]
gskkyman -g [-x days] [-cr filename] [-ct filename] [-k filename|-t tokenname] [-l label] [-kt
 {ecgen|ecdsa|ecdh}] [-ca] [-ic]
gskkyman -h|-?

 -s [-k filename]
 
 Use RENEW option 5 from menu to renew a CERTAUTH Certificate.

[INDEX](#index) 
---------------------------------------------------

## CSF


GSKSRVR trace instruction
1. S GSKSRVR 
2. TRACE CT,WTRSTART=GSKWTR 
3. TRACE CT,ON,COMP=GSKSRVR 
4. R n,JOBNAME=(yyy),OPTIONS=(LEVEL=255),WTR=GSKWTR,END 
where yyy is the name of the TCPIP stack's jobname. 
5. Recreate the error 
6. TRACE CT,OFF,COMP=GSKSRVR 
7. TRACE CT,WTRSTOP=GSKWTR 

https://www.ibm.com/docs/en/ibm-mq/9.3?topic=tz-using-gskit-trace-problems-related-certificates-keys-when-using-ams-zos
https://www.ibm.com/support/pages/how-do-you-capture-ibm-system-ssl-trace-analyse-output-sci68684
https://www.ibm.com/support/pages/how-capture-and-format-ssl-component-trace
https://www.ibm.com/docs/en/developer-for-zos/9.5.1?topic=issues-gsk-ssl-trace
https://www.ibm.com/docs/en/zvm/7.1?topic=information-gsktrace-gsktrace-utility-command
https://www.ibm.com/docs/en/zos/2.1.0?topic=information-capturing-trace-data-through-environment-variables


CSF:
Crypto Card

When you specify ICSF, you must have READ authority to the CSFIQF, CSFPKI, and CSFPKRC resources.
When you specify FROMICSF, you must have READ authority to the CSFIQF and CSFPKX resources.
When you specify SIGNWITH, you must have the following access authorities:
If the private key of the signing certificate is an ECC key that is stored in the RACF data base, you must have READ authority to the CSF1PKS, CSF1PKV, CSF1TRC, CSF1TRD, and CSFOWH resources.
If the private key of the signing certificate is stored in the ICSF PKA key data set (PKDS) or in the ICSF Token Data Set (TKDS), you require additional access based on the key type, as follows:
When the key is an RSA type, you must have READ authority to the CSFDSG resource.
When the key is an ECC type, you must have READ authority to the CSF1PKV, CSF1TRC, CSF1TRD, CSFDSG, and CSFOWH resources.

https://www.ibm.com/docs/en/zos/2.1.0?topic=ssl-racf-csfserv-resource-requirements
https://www.ibm.com/docs/en/zos/2.2.0?topic=cwcucks-setting-up-profiles-in-csfserv-general-resource-class

S GSKSRVR
F GSKSRVR,DISPLAY CRYPTO
P GSKSRVR


D ICSF,LIST,SYSPLEX=YES
D ICSF,CARDS,SYSPLEX=YES
D ICSF,KDS,SYSPLEX=YES
D ICSF,MKS,SYSPLEX=YES
D ICSF,OPT,SYSPLEX=YES

[INDEX](#index)
---------------------------------------------------

## CONSOLES


CONSOLES:

HMC - OSA ADVANCED FACILITIES
PANEL
SERVER - PUT SERVER IP AND SUBNET, PORT AND DEFAULT GATEWAY
SESSION - DEFINE THEM USING LU
VALIDATE
ACTIVATE

OPEN A SESSION TO THAT IP AND PORT
V CCCC,CONSOLE
CONSOLE SHOULD COME UP 

D C - Display Consoles

TN3270:

Same but look for LOCICC / Local Terminal definition and Activate it.

/dev/console
/dev/operlog
https://www.ibm.com/docs/en/zos/2.4.0?topic=files-system-console

LOGON APPLID
https://docs.bmc.com/docs/mcdv630/using-the-logon-command-856648226.html

[INDEX](#index)
--------------------------------------------------

## CTTRACE


CT TRACE:

CT Writer PROC:

//CTWTR PROC
//IEFPROC  EXEC PGM=ITTTRCWR,REGION=5M,TIME=1440
//TRCOUT01 DD DSNAME=yourdsn,
//            UNIT=SYSDA,DCB=(DSORG=PS),
//            SPACE=(4096,(1024,100),,CONTIG),DISP=(NEW,CATLG)

https://www.ibm.com/docs/en/ims/13.1.0?topic=commands-trace-ct-command
https://www.ibm.com/docs/en/zos/2.1.0?topic=parameters-statementsparameters-ctncccxx
WRAP
Specifies that when the system reaches the end of the data set or group of data sets, it writes over the oldest data at the start of the data set or the start of the first data set in the group. The primary extents of the data set are used.
NOWRAP
Specifies that the system stops writing to the data set or data sets when they are full. The primary and secondary extents of the data sets are used.

>>-TRACE--CT,--------------------------------------------------->

                           .-,WRAP---.                    
>----+-WTRSTART=parmlibmem-+---------+--------------+----------><
     |                     '-,NOWRAP-'              |     
     +-WTRSTOP=jobname------------------------------+     
     +-ON,COMP=irlmnm--+--------------------------+-+     
     |                 |        .---------.       | |     
     |                 |        V         |   (1) | |     
     |                 '-,SUB=(---+-DBM-+-+-)-----' |     
     |                            +-EXP-+           |     
     |                            +-INT-+           |     
     |                            +-SLM-+           |     
     |                            +-XCF-+           |     
     |                            '-XIT-'           |     
     '-OFF------------------------------------------'  

START:
TRACE CT,WTRSTART=CTWTR,NOWRAP
TRACE CT,ON,COMP=SYSTCPDA,SUB=(tcpip)    
xx,WTR=CTWTR,END
V TCPIP,tcpip,PKT,ON,FULL,IP=ipaddr|*,SRCP=port,DEST=port  

(V TCPIP,tcpip,PKT,ON,FULL,abbrev=65,IP=* to remove header)

STOP:
V TCPIP,tcpip,PKT,OFF    
TRACE CT,OFF,COMP=SYSTCPDA,SUB=(tcpip)  
TRACE CT,WTRSTOP=CTWTR,FLUSH

ALLOC FILE(SNIFFER) DA('HLQ.SNIFFER') 
ALLOCATE DDNAME(IPCSDDIR) DSNAME('hlq.DDIR') SHR

https://www.ibm.com/docs/fr/zos/2.1.0?topic=command-allocate-syntax

File:

SNIFFER:

PS
VB
8000
32000
50 Cyls

Trace:

VB
27994
27998
100 cyls

CTRACE COMP(SYSTCPDA)       LOCAL +     
   OPTIONS(( SESSION(DETAIL)         ))


[INDEX](#index)
--------------------------------------------

## ESF Printers

v.sp
F ESFstc,D,PRINTERNAME,V
F ESFstc,P,PRINTERNAME,V
F ESFstc,S,PRINTERNAME,V

JES PRINT 
https://www.ibm.com/docs/en/zos/2.1.0?topic=printers-starting-printer-defined-jes2
https://www.ibm.com/docs/en/zos/2.3.0?topic=section-t-prtnnnnn-t-rnnnnnprm-control-printer

[INDEX](#index)
----------------------------------------------

## NPF Printers
https://www.ibm.com/docs/en/zos/2.1.0?topic=introduction-network-print-facility-interfaces-vtam
https://www-40.ibm.com/servers/resourcelink/svc00100.nsf/pages/zOSV2R3SC273658/$file/halp001_v2r3.pdf
https://www.ibm.com/docs/en/zos/2.2.0?topic=introduction-overview

[INDEX](#index)
--------------------------------------------

## JES Printers

$DU,PRT - Display a JES Printer
$TA,ALL 

WS=(work_selection_criteria)
Specifies the work-selection criteria for this FSA; separate each value with a comma. See the z/OS JES2 Initialization and Tuning Reference for the valid values and defaults. For a Download for z/OS FSA, consider these values:
Q
Specifies that the FSA selects only those data sets with the same class as specified in the CLASS or QUEUE parameter of this statement.
R
Specifies that the FSA selects only those data sets with the same destination name as specified in the ROUTECDE parameter of this statement. 
If job submitters must specify the DEST=IP JCL parameter, do not specify this work-selection parameter. 
This recommendation is because job submitters cannot specify a destination name in the DEST JCL parameter when they specify the DEST=IP JCL parameter. 
See JCL parameters for information about the DEST=IP parameter.

/$TPRT1,WS=(Q)
/$T prt1,ROUTECDE=(TR1,TR2)

[INDEX](#index)
------------------------------------------------

## VPS


VPS

File Format KEY:
SITE VARrecfm LRECL=32760 RECFM=U BLKSIZE=32760
U    
0    
32760

VPS
https://help.nfc.usda.gov/publications/RFQS/74756.htm
https://www.oocities.org/smtwango/MAINFRAME/MFCOMMANDS/vpscmd.html


  VPS COMMANDS FOR MVS
   --------------------
 
     F VPS                                                              
     F VPS,ABEND                                                        
     F VPS,ACQUIRE,PRTID                                                
     F VPS,ACTIVATE,MEMBERNAME                                          
     F VPS,CANCEL,PRTID(D/J)                                            
     F VPS,CLOSELOG                                                     
     F VPS,DISPLAY,(OPTIONS)                                            
     F VPS,DIS,CMTST3ØZ       - TO DISPLAY PRINTER STATUS               
     F VPS,END                                                          
     F VPS,INACTIVATE,PRTID                                             
     F VPS,POST                                                         
     F VPS,RELEASE,PRTID                                                
     F VPS,REPEAT,PRTID
     F VPS,REPOSITION,PRTID,A=B##### (OPTIONS)                          
    #DOESN'T WORK!! F VPS,RESTART,PRTID                                                
     F VPS,SEL,PRTID,(D/C/W/F)                                          
     F VPS,SET,PRTID,(OPT#,VALUE)                                       
     F VPS,SNAP,PRTID                                                   
     F VPS,SSET,(OPTIONS)                                               
     F VPS,SSTAT,(OPTIONS)                                              
     F VPS,START,PRTID                                                  
     F VPS,STOP,PRTID,(OPTIONS)  

F VPS,DISPLAY,PRTID,TCPIP



DISPLAY

Function: Display VPS status and option information.

Description: This command provides the facility to display option and status
information pertinent to the individual VPS printers and/or the VPS
System.

Format: F VPS,DISPLAY,EXITS

Display status of VPS exits (this can be coded as EXITS to see the status
of all exits, as EXITnn to display the status of an individual exit, or as
EXITnn-nn to display the status of a range of exits).

F VPS,DISPLAY,DEFAULT

Display options in the master printer default member.

F VPS,DISPLAY,prtrid,disopt1{,disopt2....,disoptn},S=status

Display options in a particular printer member. disoptn specifies the
requested display option(s), S=status is used to filter the results of the
display command to printers matching the requested status (See page 7.2
for a complete list of status (S=) options).

Only sufficient characters to make the option unique need be specified.
AFP Display datastream conversion options.

DIAG: Printer diagnostic information.

EMAIL Display email options.

EXITS Display EXITnn keywords.

GRAPH: Graphics options.

HARDWARE: Hardware options.

MISC: Miscellaneous options.

OPER: Operational options.

OPTIONS: Printer options.

PROCESS: Processing statistics.

QUEUE: Queue dataset statistics/options.

REQUEUE: Requeue options.

SELECTION: Printer selection criteria.

STATUS: Printer status.

TCPIP: VTAM or TCP/IP related information.

VTAM: VTAM or TCP/IP related information.

ZIIP: ZIIP information.

*: All the above except DIAG.

F VPS,DISPLAY,SYSTEM

Display VPS system-wide options and status.

F VPS,DISPLAY,SYSTEM,FILESYS

Displays the VPS file system information.

F VPS,DISPLAY,SYSTEM,KEYS

Displays each valid LRS product key that was specified during VPS
initialization.

F VPS,DISPLAY,SYSTEM,AFPCACHE

Display general information about cached AFP resources. Message
VPS0931R will be issued for each resource type.

F VPS,DISPLAY,SYSTEM,AFPCACHE(FDEF=NAME|NAME*)

(PDEF=NAME|NAME*)

(OVLY=NAME|NAME*)

(PSEG=NAME|NAME*)

(FONT=NAME|NAME*)

(ID=########)

Display specific information about the specified resource(s) of the
requested type. ID subparameter will display information about the
resource associated with the specified unique ID. Messages VPS0932R,
VPS0933R, and VPS0934R will be issued for each matching resource.

F VPS,DISPLAY,SYSTEM,MODULE,modid

Display information about a specific VPS module (e.g., load address,
entry address, length).

F VPS,DISPLAY,SYSTEM,TASK

Display the status of each VPS task (system and printer tasks). Message
VPS0959R will be issued for each VPS task.

F VPS,DISPLAY,SYSTEM,WHERE,address

Displays the module and offset related to a specified address.

F VPS,DISPLAY,SYSTEM,ZIIP

Display the VPS ZIIP information.

F VPS,DISPLAY,S=E

Display a list of all printers that are in an EDRAINED status.

F VPS,DISPLAY,VPSPRT*,S=E,TCP

Display the VTAM or TCP/IP related information for printers named
with a prefix of VPSPRT, that are in EDRAINED status.
Comments: STATUS is the default display option for a printer display if no options
are specified.

Example: F VPS,DISPLAY,VPSPRT99,ST,SEL

Display status information and selection criteria for printer VPSPRT99.

END

EXPIRE

INACTIVATE

Function: Normally terminate VPS.

Description: This command will notify VPS to initiate normal termination processing.

Format: F VPS,END

Comments: This command has no operands or prtrid specification.
VPS will not terminate until all printers that are currently busy complete
the job that they are processing.

Example: F VPS,END

Terminate VPS normally

[INDEX](#index)

------------------------------------------------

## SMF

https://www.ibm.com/docs/en/zos/2.1.0?topic=smf-records
https://www.ibm.com/docs/en/zos/2.1.0?topic=analyzer-collecting-smf-records
https://www.ibm.com/docs/en/zos/2.4.0?topic=smf-record-general-information-best-practices
https://www.ibm.com/docs/en/zos/2.4.0?topic=statements-smfconfig-statement

DISPLAY SMF FILES IN USE
https://www.ibm.com/docs/en/zos/2.4.0?topic=command-displaying-smf-data-smf

DYNAMICALLY ADD SMF RECORDS
https://www.ibm.com/docs/en/zos/2.2.0?topic=member-changing-smf-recording

DUMP SMF
https://www.ibm.com/docs/en/zos/2.1.0?topic=ifasmfdp-running-smf-data-set-dump-program

SMF118
https://www.ibm.com/docs/en/zos/2.3.0?topic=reference-type-118-smf-records
https://www.pacsys.com/smf/smf118_v1r13.htm

SMF118 Subtypes
https://www.ibm.com/docs/en/zos/2.1.0?topic=records-standard-subtype-record-numbers

Subtype 76
https://www.ibm.com/docs/en/zos/2.1.0?topic=records-record-type-118-76-tcpip-statistics

SMF119 Format
https://www.ibm.com/docs/en/zos/2.1.0?topic=records-common-type-119-smf-record-format#commonamf

SMF119 Subtypes
https://www.ibm.com/docs/en/zos/2.1.0?topic=records-smf-119-record-subtypes

Subtype 21
https://www.ibm.com/docs/en/zos/2.1.0?topic=t1sr-tn3270e-telnet-server-sna-session-termination-record-subtype-21#serversna

Subtype 23
https://www.ibm.com/docs/en/zos/2.1.0?topic=t1sr-tso-telnet-client-connection-termination-record-subtype-23#telnetcc

Subtype 77
https://www.ibm.com/docs/en/zos/2.1.0?topic=records-record-type-119-77-tcpip-statistics


E35
https://www.ibm.com/docs/en/zos/2.4.0?topic=exits-e35-user-exit-changing-records

## ICETOOL

https://www.ibm.com/docs/kk/zos/2.1.0?topic=do-operand-descriptions-2



[INDEX](#index)

-----------------------------------

# FILE TRANSFERS

## XMIT

SYNTAX

```
xmit user.node dsn('hlq.ql') outdsn('hlq.ql')
receive indsn('hlq.ql')
```

[INDEX](#index)
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


[INDEX](#index)
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

[INDEX](#index)
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

[INDEX](#index)
--------------------------------

## SSH

### SFTP

```
ssh -vvv -c aes256-cbc -p 8022 8.8.8.8
sftp -c aes256-cbc -P 8022 8.8.8.8
Sftp -o "StrictHostkeyChecking no"
```

https://www.ibm.com/docs/en/zos/2.4.0?topic=guide-accessing-mvs-data-sets-within-sftp
https://www.ibm.com/docs/en/zos/2.1.0?topic=utility-invoking-bpxbatch-in-batch-job

```
# sftp -h
usage: sftp -B buffer_size -b batchfile -c cipher
          -D sftp_server_path -F ssh_config -i identity_file -l limit
          -o ssh_option -P port -R num_requests -S program
          -s subsystem | sftp_server host
       sftp user@host:file ...
       sftp user@host:dir/
       sftp -b batchfile user@host
```

https://www.ibm.com/docs/en/zos/2.2.0?topic=ssftp-options

https://www.ibm.com/docs/en/zos/2.2.0?topic=program-host-key-checking

https://www.ibm.com/docs/en/integration-bus/10.0?topic=sftp-known-host-checking

SSH

```
usage: ssh options user@host command
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
  -D bind-addr:port     Enables dynamic application-level port forwarding.
  -e char     Set escape character; ``none'' = disable (default: ~).
  -E file     Append debug logs to file instead of standard error.
  -F config   Config file (default: ~/.ssh/config).
  -i file     Identity for public key authentication.
  -J user@host:port     Shortcut to specify a ProxyJump configuration direc
tive.
tive.
  -L bind_address:port:host:hostport   Forward local port to remote address.
  -L bind_address:port:remote_socket   Forward local port to remote socket.
  -L local_socket:host:hostport          Forward local socket to remote address.
  -L local_socket:remote_socket          Forward local socket to remote socket.
  -l user     Log in using this user name.
  -m macs     Specify MAC algorithms.
  -O ctl-cmd  Control an active connection multiplexing master process.
  -o 'option' Process the option as if it was read from a configuration file.
  -p port     Port to connect to on the remote host.
  -Q cipher | cipher-auth | mac | kex | key | key-cert | key-plain | protocol-ve
rsion   Queries ssh for the supported algorithms.
  -R bind_address:port:host:hostport   Forward remote port to local address.
  -R bind_address:port:local_socket    Forward remote port to local socket.
  -R remote_socket:host:hostport         Forward remote socket to local address.
  -R remote_socket:local_socket          Forward remote socket to local socket.
  -R bind_address:port                 Forward remote port to using SOCKS.
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
usage: ssh-keyscan -f file -p port -T timeout -t type
                   host | addrlist namelist ...
```

KEYGEN

```
ssh-keygen -t rsa
ssh-keygen -t dsa
```

```
ssh-keygen -i -f testkey.putty.pub >>  /USERIDHOME/.ssh/authorized_keys
ssh-keygen -i -f authorized_keys >>  /u/dbbg/.ssh/authorized_keys2
```

zOS Open SSH uses BASE64 encoding. 


BE CAREFUL on how it is uploaded. When you upload a key file, it might get encoded in a different way.
ssh-keygen -i -m RFC4716 -f /u/user/pub >>  /u/user/pubibm

```
ssh-keygen help
```

```
usage: ssh-keygen options
  ssh-keygen -q -b bits -t type -o -a rounds -N new_passphrase -C comment -f output_keyfile
  ssh-keygen -p -P old_passphrase -N new_passphrase -f keyfile
  ssh-keygen -i -m key_format -f input_keyfile
  ssh-keygen -e -m key_format -f input_keyfile
  ssh-keygen -e -m key_format -f input_keyfile
  ssh-keygen -y -f input_keyfile
  ssh-keygen -c -P passphrase -C comment -f keyfile
  ssh-keygen -l -v -E fingerprint_hash -f input_keyfile
  ssh-keygen -B -f input_keyfile
  ssh-keygen -F hostname -f known_hosts_file -l
  ssh-keygen -H -f known_hosts_file
  ssh-keygen -R hostname -f known_hosts_file
  ssh-keygen -r hostname -f input_keyfile -g
  ssh-keygen -G output_file -v -b bits -M memory -S start_point
  ssh-keygen -T output_file -f input_file -v -a rounds -J num_lines -j start_line -K checkpt -W generator
  ssh-keygen -s ca_key -I certificate_identity -h -U -n principals -O option -V validity_interval -z serial_number¨ file
...
  ssh-keygen -L -f input_keyfile
  ssh-keygen -A
  ssh-keygen -k -f krl_file -u -s ca_public -z version_number file ...
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

[INDEX](#index)
---------------------------------------------------------------------------------------------------

# RACF

## Common

https://www.ibm.com/docs/en/zos/2.4.0?topic=reference-racf-command-syntax

https://www.ibm.com/docs/en/zos/2.2.0?topic=reference-racf-tso-commands

Commands:

RLIST
https://www.ibm.com/docs/en/zos/2.4.0?topic=syntax-rlist-list-general-resource-profile#rlist

RACDCERT
https://www.ibm.com/docs/en/zos/2.4.0?topic=syntax-racdcert-manage-racf-digital-certificates#radcertg

Refresh Classes:
https://www.ibm.com/docs/en/zos/2.4.0?topic=racf-refreshing-classes

Roles:

https://www.ibm.com/docs/en/zos/2.2.0?topic=guide-racf-auditor

https://www.ibm.com/products/zsecure-audit

https://www.ibm.com/docs/en/szs/2.2.1?topic=racf-overview


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

[INDEX](#index)
-----------------------------------------

## Certificates

Certificate Work:

https://www.ibm.com/docs/en/zos/2.1.0?topic=applications-setting-up-your-certificate-environment

### RACF INSERT CERTIFICATE:

```
RACDCERT CERTAUTH ADD('dataset') TRUST +
WITHLABEL('label')
```

### RACF REMOVE FROM RING:

```
RACDCERT ID(id) REMOVE(CERTAUTH LABEL('label') RING(ringname)
```

ACTIVATE CLASSES:

'''
SETROPTS CLASSACT(DIGTCERT DIGTRING)
'''

REFRESH CLASSES:

'''
SETROPTS RACLIST(DIGTCERT DIGTRING) REFRESH
'''

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

ROOT Certificate Creation:

'''
RACDCERT CERTAUTH GENCERT +      
    SUBJECTSDN(CN('ROOT')) +
    WITHLABEL('ROOT') +      
    KEYUSAGE(CERTSIGN) +         
    NOTAFTER(DATE(yyyy-mm-dd))   
'''

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

[INDEX](#index)
---------------------------------------------------------------------------------------------------------
---------------------------------------------

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

[INDEX](#index)
----------------------------------

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

 Export {logonid|logonid.suffix}
       DSname(data-set-name)
       [Label(label)]
       [Format(CERTDER|CERTB64|PKCS12DER|PKCS12B64|PKCS7DER|PKCS7B64)]
       [Password(password)]
       
Command Input:
EXPORT FRANK01.CERT DSNAME(MYCERT)

https://www.ibm.com/docs/en/zos/2.1.0?topic=gime-importing-certificate-from-file-as-trusted-ca-certificate

https://techdocs.broadcom.com/us/en/ca-mainframe-software/security/ca-acf2-for-z-os/16-0/administrating/digital-certificate-support.html

https://techdocs.broadcom.com/us/en/ca-mainframe-software/security/ca-acf2-for-z-os/16-0/administrating/digital-certificate-support/process-digital-certificates-with-ca-acf2.html

https://knowledge.broadcom.com/external/article/18198/does-acf2-support-virtual-keyrings.html

https://knowledge.broadcom.com/external/article/94292/how-do-we-specify-keyring-name-in-a-batc.html


[INDEX](#index)
---------------------------------------------------------------------------------------------------------
---------------------------------------------------------------------------------------------------------
---------------------------------------------------------------------------------------------------------

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

[INDEX](#index)
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

[INDEX](#index)
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

PAGE DATASETS

D ASM
PA NONVIO=SYS1.NEW.PAGE

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
 

