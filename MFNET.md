# MFNET UTILS

### Purpose of this document

This document is meant to be a reference guide for zOS practicioners. Oriented mostly to Communications Server configuration, troubleshooting and related applications.

### This is another node




## File Transfer
[XMIT](#xmit)
[ConnectDirect](#connect direct)
[WinSCP](#winscp)
[FTP](#ftp)


## JCL
[REUSABLE JCL](#reusable)
[Parameters](#parameters)
























-----------------------------------------------------------------------------------------------------------------------------

### XMIT

SYNTAX

```
xmit user.node dsn('hlq.ql') outdsn('hlq.ql')
receive indsn('hlq.ql')
```

### Connect Direct

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

### WinSCP

winscp.exe /console

open hostname
put C:/sadsad/asdad.txt HLQ.DATASET    // NO QUOTES

open -passive=off ftpes://${useridpass}:$cpassword@$hostname/
call site file=jes
ascii  //  binary
put ftpjcl.txt
exit

### FTP

FTP USEFUL

SITE        -FTP default
QUOTE SITE  -Windows
LOCSITE     -zOS
CALL SITE   -WinSCP

https://www.ibm.com/support/pages/sitelocsite-commands-mvs-ftp


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

#### FTP to JES:
open hostname
userid
password
prompt off
quote site file=jes
dir

SITE / LOCSITE / QUOTE SITE / CALL SITE

SITE VARrecfm LRECL=32760 RECFM=U BLKSIZE=32760



-----------------------------------------------------------------------------------------------------------------------------

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

--------------------------------------------



--------------------------------------------



--------------------------------------------



--------------------------------------------
