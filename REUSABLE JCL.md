# MFNET REUSABLE JCL

## Purpose of this document

This is a repository of widely used JCL.

-----------------------------------------

# INDEX

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

```
//DD1 DD DSNAME=ALP,DISP=(,KEEP),VOLUME=SER=44321, 
// UNIT=3400-6,DCB=(RECFM=FB,LRECL=240,BLKSIZE=960, 
// DEN=1,TRTCH=C)
```

```
1 Cyl = 15 Tracks 
1 Track = 25 Blocks

1 Cylinder = 55,996 * 15  =  839,940 bytes.
so 1000 cylinders = 839,940 * 1000   
1 Megabyte =  1,048,576 (2 to the 20th power) bytes.
1000 cylinders = (839,940 * 1000 ) / 1,048,576  = 801.029 MB
1 terabyte =  2 to the 40th power or approximately a thousand billion bytes (that is, a thousand gigabytes).
1000 cylinders = (839,940 * 1000 ) / (1,048,576 * 1,048,576 )  = .000763 Terabytes
```

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
# EXAMPLES

-----------------------------------------------------------------------------------------------------------------------------

## ACF2

### CERTIFICATE INVENTORY ACF2


```
//STEP01   EXEC PGM=IKJEFT01
//SYSTSPRT DD DISP=SHR,DSN=yourdsn
//SYSTSIN  DD *
ACF
T PROF(USER) DIV(CERTDATA)
L LIKE(-)
```

### KEYRING INVENTORY ACF2

```
//STEP01   EXEC PGM=IKJEFT01
//SYSTSPRT DD DISP=SHR,DSN=yourdsn
//SYSTSIN  DD *
ACF
T PROF(USER) DIV(KEYRING)
L LIKE(-)
```

### USER INVENTORY ACF2

```
//STEP01   EXEC PGM=IKJEFT01
//SYSTSPRT DD DISP=SHR,DSN=yourdsn
//SYSTSIN  DD *
ACF
L LIKE(-)
```

### USER PASSWORD CHANGE ACF2

```
//STEP01   EXEC PGM=IKJEFT01
//SYSTSPRT DD DISP=SHR,DSN=yourdsn
//SYSTSIN  DD *
ACF
CHANGE userid PASS(password)
```


### CERTIFICATE INSERT
### CERTIFICATE CONNECT
### RDA RULE
### IRR RULE

```
//STEP01   EXEC PGM=IKJEFT01
//SYSTSPRT DD DISP=SHR,DSN=yourdsn
//SYSTSIN  DD *
ACF

```


-----------------------------------------------------------------------------------------------------------------------------


### ADRDSSU

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
	
-----------------------------------------------------------------------------------------------------------------------------


### SDSF Commands:

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
ULOG
/D IPLINFO
PRINTFILE DATAOUT
PRINT
PRINT CLOSE
END
```

-----------------------------------------------------------------------------------------------------------------------------


### IEBCOPY - Copy MODULEs

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

### IEBCOPY - COMPRESS

```
//COMPRESS    EXEC    PGM=IEBCOPY
//A    DD  DSNAME='Pacanowska',DISP=OLD
//B    DD  DSNAME='Pacanowska',DISP=OLD
//SYSIN DD *
       COPY OUTDD=B,INDD=A
```

-----------------------------------------------------------------------------------------------------------------------------

## IDCAMS

### IDCAMS - COPY to GDG

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

### IDCAMS - DELETE 

```
//STEP2    EXEC PGM=IDCAMS
//SYSPRINT DD  SYSOUT=*
//SYSIN    DD *
   DELETE dsnname
/*
```

### IDCAMS - CREATE PAGE DATASET

```
//CREATE EXEC PGM=IDCAMS     
//SYSPRINT DD  SYSOUT=*      
//SYSIN    DD   *            
 DEFINE PAGESPACE (  -       
 NAME(SYS1.NEW.PAGE) -       
 CYLINDERS(20) -             
 VOLUME(volume))             
```

### IDCAMS - GDG BATCH

```
//STEP1    EXEC PGM=IDCAMS
//SYSPRINT DD SYSOUT=*
//SYSIN    DD *
 DEFINE GDG(NAME(HLQ.GDGBASE) -
 LIMIT(10) -
 NOEMPTY -
 SCRATCH)
```

### IDCAMS - CREATE INDEXED VSAM FILES

```
//VSAM EXEC PGM=IDCAMS
//SYSPRINT DD SYSOUT=*
//SYSIN DD *
 DEFINE CLUSTER(                                   -
 NAME(yourcluster)                -
 INDEXED                                            -
 NOIMBED                                            -
 REUSE                                              -
 NOREPLICATE                                        -
 FREESPACE(10 5)                                   -
 KEYS (27 0)                                        -
 RECORDSIZE(32 78) -
 SHAREOPTIONS(2)) -
 DATA                                               -
 (CONTROLINTERVALSIZE(4096)                         -
 TRK(500)                                           -
 NAME(yourcluster.DATA))
```

### IDCAMS - CREATE ZFS FILE

```
//FILECREA EXEC PGM=IDCAMS,REGION=0M 
//SYSPRINT DD SYSOUT=* 
//SYSIN    DD *
    DEFINE CLUSTER( - 
             NAME(yourzfs) -     
             VOLUME(volume) -
             LINEAR -
             CYL(100 20) - 
             SHAREOPTIONS(3))       
/*  
//FORMAT   EXEC PGM=IOEAGFMT,REGION=0M,COND=(0,LT,FILECREA),
//            PARM='-aggregate yourzfs -compat'
//SYSPRINT DD SYSOUT=*
```

-----------------------------------------------------------------------------------------------------------------------------

### FTP BATCH

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


### FTPS BATCH (WITHOUT AT-TLS)

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

-----------------------------------------------------------------------------------------------------------------------------


### IKJEFT1B - EXECUTE REXX from external Library

```
//REPOFTP   EXEC PGM=IKJEFT1B,TIME=1439                                          
//SYSEXEC   DD  DISP=SHR,DSN=HLQ.QL                                 
//SYSTSPRT  DD  SYSOUT=*                                                        
//SYSTSIN   DD  *                                                               
  %REXXMEM                                                                     
/*   
```

### IKJEFT01 - TSO EXEC

```
//TSOEX     EXEC PGM=IKJEFT01                                                   
//SYSEXEC   DD DSN=HLQ.QL,DISP=SHR                                   
//SYSTSPRT  DD SYSOUT=*                                                         
//SYSPRINT  DD SYSOUT=*                                                         
//SYSTSIN   DD *                                                                
  EXEC 'HLQ.QL(REXXMEM)'                                              
//     
```

### IPCS BATCH

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

-----------------------------------------------------------------------------------------------------------------------------

### PING BATCH

```
//STEP01    EXEC  PGM=IKJEFT01
//SYSTSPRT  DD  DISP=SHR,DSN=output
//SYSTSIN   DD  *
PING 8.8.8.8
```

-----------------------------------------------------------------------------------------------------------------------------

### SFTP BATCH

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

-----------------------------------------------------------------------------------------------------------------------------

### SMTP

When sending Attachments, SYSUT1 needs to be in a dataset and it has to have the same LRECL as the file you are attaching

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

-----------------------------------------------------------------------------------------------------------------------------

### SMF Records ICETOOL

https://www.ibm.com/docs/en/zos/2.1.0?topic=profile-smfinit-smfterm-statements

Type 20

```
//STEP1  EXEC  PGM=ICETOOL                          
//TOOLMSG  DD SYSOUT=*                              
//DFSMSG   DD SYSOUT=*                              
//RAWSMF   DD DISP=SHR,DSN=SMFDATA

//SORTSMF  DD DSN=SMFSORT,      
//         DISP=SHR,UNIT=SYSDA,                
//         SPACE=(CYL,(50,10),RLSE)            
//PRINT    DD SYSOUT=*                         
//VREPT    DD SYSOUT=*                         
//* ST 21 - 275                                
//* ST 2 - 300                                 
//* HEADER('BY') ON(150,4,BI) -                
//* HEADER('BY') ON(154,8,BI) -                
//* HEADER('BY') ON(162,8,BI)                  
//TOOLIN   DD *                                
COPY FROM(RAWSMF) TO(SORTSMF) USING(VLSH)      

DISPLAY FROM(SORTSMF) LIST(VREPT) -            
       TITLE('SMF TYPE-119 SUBTYPE 20') -      
       BETWEEN(0) -                            
       HEADER('TIME') ON(7,4,TM1,E'99:99:99') -
       HEADER('') ON(30,1,CH)-                        
       HEADER('DATE') ON(11,4,DT1,E'9999/99/99') -    
       HEADER('') ON(30,1,CH)-                        
       HEADER('SYSID') ON(15,4,CH) -                  
       HEADER('') ON(30,1,CH)-                        
       HEADER('IP') ON(141,1,BI,E'999.') -            
       HEADER('') ON(142,1,BI,E'999.') -              
       HEADER('') ON(143,1,BI,E'999.') -              
       HEADER('') ON(144,1,BI,E'999') -               
       HEADER('') ON(30,1,CH)-                        
       HEADER('LU NAME') ON(109,8,CH) -               
       HEADER('') ON(30,1,CH)-                        
       HEADER('APPLICATION') ON(117,8,CH)             
//VLSHCNTL DD *                                       
  OPTION COPY,VLSHRT                                  
  INCLUDE COND=((((6,1,BI,EQ,+119,AND,23,2,BI,EQ,+20),
         AND,45,4,BI,GT,0),
         AND,7,4,BI,GT,0), 
         AND,11,4,PD,GT,0) 
  END              
```


Type 21

```
DISPLAY FROM(SORTSMF) LIST(VREPT) -                
       BETWEEN(0) -                                
       HEADER('TIME') ON(7,4,TM1,E'99:99:99') -    
       HEADER('') ON(197,1,CH)-                    
       HEADER('DATE') ON(11,4,DT1,E'9999/99/99') - 
       HEADER('') ON(197,1,CH)-                    
       HEADER('SYSID') ON(15,4,CH) -               
       HEADER('') ON(197,1,CH)-                    
       HEADER('IP') ON(165,1,BI,E'999.') -         
       HEADER('') ON(166,1,BI,E'999.') -           
       HEADER('') ON(167,1,BI,E'999.') -           
       HEADER('') ON(168,1,BI,E'999') -            
       HEADER('') ON(197,1,CH)-                    
       HEADER('LU NAME') ON(133,8,CH) -            
       HEADER('') ON(197,1,CH)-                    
       HEADER('APPLICATION') ON(141,8,CH) -        
       HEADER('') ON(197,1,CH)-                    
       HEADER('HOSTNAME') ON(189,8,CH)                
//VLSHCNTL DD *                                       
  OPTION COPY,VLSHRT                                  
  INCLUDE COND=((((6,1,BI,EQ,+119,AND,23,2,BI,EQ,+21),
         AND,45,4,BI,GT,0),                           
         AND,7,4,BI,GT,0),                            
         AND,11,4,PD,GT,0)                            
  END                           
```