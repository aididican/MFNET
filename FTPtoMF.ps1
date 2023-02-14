
$dir = "D:\GitHub\MFNET\LAST\LATEST\LATEST"
$racfjcl = "$pwd\racfjcl.txt"
$pwd = "D:\GitHub\MFNET\LAST\LATEST\LATEST"
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Function Startup-PS {
Write-Host "
Please select an option from the menu:"

Write-Host "To change your password in a " -NoNewline
Write-Host "SINGLE" -ForegroundColor GREEN -NoNewline
Write-Host " system. Enter " -NoNewline
Write-Host "SINGLE" -ForegroundColor GREEN

Write-Host "To change your password in " -NoNewline
Write-Host "ALL" -ForegroundColor RED -NoNewline
Write-Host " systems. Enter " -NoNewline
Write-Host "ALL" -ForegroundColor RED

Write-Host "To submit your own " -NoNewline
Write-Host "JCL" -ForegroundColor YELLOW -NoNewline
Write-Host " or choose one from a set of fixed ones, enter " -NoNewline
Write-Host "JCL" -ForegroundColor YELLOW

$selection = Read-Host -Prompt 'Please make your selection'
$selection = $selection.ToUpper()

if ($selection -match "SINGLE")
{
Single-System
}
elseif ($selection -match "ALL")
{
All-Systems
}
elseif ($selection -match "JCL")
{
JCL-List
}

}

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Function JCL-List {
Write-Host "To use your " -NoNewline
Write-Host "OWN JCL" -ForegroundColor RED -NoNewline
Write-Host ", Enter " -NoNewline
Write-Host "OWN" -ForegroundColor RED

Write-Host "To select a  " -NoNewline
Write-Host "REPORT" -ForegroundColor GREEN -NoNewline
Write-Host ", Enter " -NoNewline
Write-Host "REPORT" -ForegroundColor GREEN

Write-Host "To select a  " -NoNewline
Write-Host "REUSABLE" -ForegroundColor GREEN -NoNewline
Write-Host " JCL, Enter " -NoNewline
Write-Host "REUSABLE" -ForegroundColor GREEN

$selection3 = Read-Host -Prompt "Please enter your selection (OWN, REPORT, REUSABLE)"
$selection3 = $selection3.ToUpper()

if ($selection3 -match "OWN")
{
Own-JCL
}
elseif ($selection3 -match "REPORT")
{
Report-JCL
}
elseif ($selection3 -match "REUSABLE")
{
Reusable-JCL
}
}


#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------



Function Own-JCL {

Write-Host "Please enter your JCL in the TEXT file."
notepad.exe $pwd\jcltosub.txt

$hostname = Read-Host -Prompt 'Input your hostname'


Write-Host "
You will now submit a JCL in: $hostname
"
Write-Host "Please Input your " -NoNewline
Write-Host " USERID " -ForegroundColor GREEN -NoNewline
$userid = Read-Host

Write-Host "
The Password rules for the Mainframe only allow 8-character-long passwords.

The Old and New password can only be entered in Alphanumeric characters (letters and numbers).

Please remain compliant with our policy. Thank you!
"
Write-Host "Please Input your" -NoNewline
Write-Host " CURRENT PASSWORD " -ForegroundColor RED -NoNewline
$cpassword1 = Read-Host -AsSecureString 
while ($cpassword1.length -ne 8) 
{
    Write-Output "Make sure you spelled your current password correctly."
    Write-Host "Please Input your" -NoNewline
    Write-Host " CURRENT PASSWORD " -ForegroundColor RED -NoNewline
    $cpassword1 = Read-Host -AsSecureString
}
$bstr = [System.Runtime.InteropServices.Marshal]::SecureStringToBSTR($cpassword1)
$cpassword = [System.Runtime.InteropServices.Marshal]::PtrToStringAuto($bstr)

"open $hostname
user " + "$userid $cpassword
ascii
quote site file=jes  
lcd $dir     
ls
put jcltosub.txt
mget *
exit
" | ftp -i -n -d
}



#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------



Function CMD-File ($userid) {
"open $hostname
user " + "$userid $cpassword
ascii
quote site file=jes  
lcd $dir     
ls
put ftpjcl.txt
mget *
exit
" | ftp -i -n -d
}

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


Function Ftp-File ($userid) {
    & 'C:\Program Files (x86)\WinSCP\WinSCP.com' `
      /log="$pwd\WinSCP.log" /ini=nul `
      /command `
        "open -passive=off ftp://${userid}:$cpassword@$hostname/" `
        "call site file=jes NOJESGETBYDSN" `
        "ascii" `
        "lcd C:\Github\Personal\HCL\MFNET\LATEST" `
        "put ftpjcl.txt output" `
        "exit"
    }

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


Function Ftps-File ($userid) {
    & 'C:\Program Files (x86)\WinSCP\WinSCP.com' `
      /log="$pwd\WinSCP.log" /ini=nul `
      /command `
        "open -passive=off ftpes://${userid}:$cpassword@$hostname/" `
        "call site file=jes" `
        "ascii" `
        "put ftpjcl.txt" `
        "exit"
    }

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


Function Conn-Test {
$hostfile = "$pwd\hosts.txt"
$host1 = Read-Host -Prompt "Please input the host you want to reach"
ac $hostfile $host1

$names = Get-Content "$pwd\hosts.txt"

foreach ($name in $names) {
$pingresult = Test-Connection -ComputerName $name -Count 1 -ErrorAction SilentlyContinue
    if ( $pingresult -ne $NULL )
    {
		Write-Host "$name is Online" -ForegroundColor Green
    }
    else 
    {
        Write-Host "$name is NOT ONLINE" -ForegroundColor Red
    }
    
}

del $hostfile

}

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


Function All-Systems {
Write-Host "
This will change your password in ALL the systems. 

Make sure your Current Password is the same accross all LPARs.

"

Read-Host -Prompt "Press any key to continue..."

$jclfile = "$pwd\ftpjcl.txt"

if (Test-Path $jclfile -ErrorAction SilentlyContinue) {
  Remove-Item $jclfile
}
else
{
$null
}


$userida = Read-Host -Prompt 'Input your User ID for A'

$useridb = Read-Host -Prompt 'Input your User ID for B'

$useridc = Read-Host -Prompt 'Input your User ID for C'


Write-Host "
The Password rules for the Canada Life Mainframe only allow 8-character-long passwords.

The Old and New password can only be entered in Alphanumeric characters (letters and numbers).

Please remain compliant with our policy. Thank you!
"
Write-Host "Please Input your" -NoNewline
Write-Host " CURRENT PASSWORD " -ForegroundColor RED -NoNewline
$cpassword1 = Read-Host -AsSecureString 
while ($cpassword1.length -ne 8) 
{
    Write-Output "Make sure you spelled your current password correctly."
    Write-Host "Please Input your" -NoNewline
    Write-Host " CURRENT PASSWORD " -ForegroundColor RED -NoNewline
    $cpassword1 = Read-Host -AsSecureString
}
$bstr = [System.Runtime.InteropServices.Marshal]::SecureStringToBSTR($cpassword1)
$cpassword = [System.Runtime.InteropServices.Marshal]::PtrToStringAuto($bstr)

Write-Host "Please Input your" -NoNewline
Write-Host " NEW PASSWORD " -ForegroundColor YELLOW -NoNewline
$npassword1 = Read-Host -AsSecureString 

while ($npassword1.length -ne 8) 
{
    Write-Output "Make sure your new password is compliant with our password policy."
    Write-Host "Please Input your" -NoNewline
    Write-Host " NEW PASSWORD " -ForegroundColor YELLOW -NoNewline
    $npassword1 = Read-Host -Prompt 'Input your new password' -AsSecureString
}
$bstr1 = [System.Runtime.InteropServices.Marshal]::SecureStringToBSTR($npassword1)
$npassword = [System.Runtime.InteropServices.Marshal]::PtrToStringAuto($bstr1)

while ($npassword -match $cpassword) 
{
Write-Host "Your New password cannot be the same as your old password.
    
Please restart the Password Change Process.
"
Write-Host "
The Password rules for the Mainframe only allow 8-character-long passwords.

The Old and New password can only be entered in Alphanumeric characters (letters and numbers).

Please remain compliant with our policy. Thank you!
"

Write-Host "Please Input your" -NoNewline
Write-Host " CURRENT PASSWORD " -ForegroundColor RED -NoNewline
$cpassword1 = Read-Host  -AsSecureString
while ($cpassword1.length -ne 8) 
{
    Write-Output "Make sure you spelled your current password correctly."
    Write-Host "Please Input your" -NoNewline
    Write-Host " CURRENT PASSWORD " -ForegroundColor RED -NoNewline
    $cpassword1 = Read-Host -AsSecureString
}
$bstr = [System.Runtime.InteropServices.Marshal]::SecureStringToBSTR($cpassword1)
$cpassword = [System.Runtime.InteropServices.Marshal]::PtrToStringAuto($bstr)



Write-Host "Please Input your" -NoNewline
Write-Host " NEW PASSWORD " -ForegroundColor YELLOW -NoNewline
$npassword1 = Read-Host -AsSecureString
while ($npassword1.length -ne 8) 
{
    Write-Output "Make sure your new password is compliant with our password policy."
    Write-Host "Please Input your" -NoNewline
    Write-Host " NEW PASSWORD " -ForegroundColor YELLOW -NoNewline
    $npassword1 = Read-Host -AsSecureString
}
$bstr1 = [System.Runtime.InteropServices.Marshal]::SecureStringToBSTR($npassword1)
$npassword = [System.Runtime.InteropServices.Marshal]::PtrToStringAuto($bstr1)
}

Write-Host "Please Re-enter your" -NoNewline
Write-Host " NEW PASSWORD " -ForegroundColor YELLOW -NoNewline
$nnpassword1 = Read-Host -AsSecureString
$bstr1 = [System.Runtime.InteropServices.Marshal]::SecureStringToBSTR($nnpassword1)
$nnpassword = [System.Runtime.InteropServices.Marshal]::PtrToStringAuto($bstr1)

while ($nnpassword -ne $npassword) 
{
    Write-Output "Make sure you typed your new password correctly"
    Write-Host "Please Re-enter your" -NoNewline
    Write-Host " NEW PASSWORD " -ForegroundColor YELLOW -NoNewline
    $nnpassword1 = Read-Host -AsSecureString
    $bstr1 = [System.Runtime.InteropServices.Marshal]::SecureStringToBSTR($nnpassword1)
    $nnpassword = [System.Runtime.InteropServices.Marshal]::PtrToStringAuto($bstr1)
}
    
if (Test-Path $jclfile -ErrorAction SilentlyContinue) {
  Remove-Item $jclfile
}
else
{
$null
}
Write-Host "
Processing A
"

Read-Host -Prompt "Press any key to continue..."

$hostname = "systema" 
$account = "(0000,0000)"
$userid309ap = "$userida" + "P"
$userid309ap = $useridap.ToUpper()

if (Test-Path $jclfile -ErrorAction SilentlyContinue) {
  Remove-Item $jclfile
}
else
{
$null
}
ac $jclfile "//$useridap JOB $account,'$userida',NOTIFY=&SYSUID,CLASS=A," 
ac $jclfile "//            MSGCLASS=H,MSGLEVEL=1,"
ac $jclfile "//            PASSWORD=($cpassword,$npassword)"
ac $jclfile "//STEP01   EXEC PGM=IEFBR14" 

Ftp-File -useridpass $userida > $null

if (Test-Path $jclfile -ErrorAction SilentlyContinue) {
  Remove-Item $jclfile
}
else
{
$null
}
Write-Host "
Processing B
"

Read-Host -Prompt "Press any key to continue..."

$hostname = "systemb" 
$account = "(000,0000)"
$useridgwldp = "$useridgwld" + "P"
$useridgwldp = $useridgwldp.ToUpper()

if (Test-Path $jclfile -ErrorAction SilentlyContinue) {
  Remove-Item $jclfile
}
else
{
$null
}
ac $jclfile "//$useridbp JOB $account,'$useridb',NOTIFY=&SYSUID,CLASS=A," 
ac $jclfile "//            MSGCLASS=H,MSGLEVEL=1,"
ac $jclfile "//            PASSWORD=($cpassword,$npassword)"
ac $jclfile "//STEP01   EXEC PGM=IEFBR14" 

Ftp-File -useridpass $useridgwld > $null

if (Test-Path $jclfile -ErrorAction SilentlyContinue) {
  Remove-Item $jclfile
}
else
{
$null
}
Write-Host "
Processing C
"

Read-Host -Prompt "Press any key to continue..."

$hostname = "systemc" 
$account = "(0000,0000)"
$userid309cp = "$useridc" +"P"
$userid309cp = $useridcp.ToUpper()

if (Test-Path $jclfile -ErrorAction SilentlyContinue) {
  Remove-Item $jclfile
}
else
{
$null
}
ac $jclfile "//$useridcp JOB $account,'$useridc',NOTIFY=&SYSUID,CLASS=A," 
ac $jclfile "//            MSGCLASS=H,MSGLEVEL=1,"
ac $jclfile "//            PASSWORD=($cpassword,$npassword)"
ac $jclfile "//STEP01   EXEC PGM=IEFBR14" 

Ftp-File -useridpass $useridc > $null

if (Test-Path $jclfile -ErrorAction SilentlyContinue) {
  Remove-Item $jclfile
}
else
{
$null
}


if (Test-Path $jclfile -ErrorAction SilentlyContinue) {
  Remove-Item $jclfile
}
else
{
$null
}
}


# -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


Function Single-System {
$hostname = Read-Host -Prompt 'Input your hostname'


Write-Host "
You will now change your password in: $hostname
"
Write-Host "Please Input your " -NoNewline
Write-Host " USERID " -ForegroundColor GREEN -NoNewline
$userid = Read-Host

Write-Host "
The Password rules for the Mainframe only allow 8-character-long passwords.

The Old and New password can only be entered in Alphanumeric characters (letters and numbers).

Please remain compliant with our policy. Thank you!
"
Write-Host "Please Input your" -NoNewline
Write-Host " CURRENT PASSWORD " -ForegroundColor RED -NoNewline
$cpassword1 = Read-Host -AsSecureString 
while ($cpassword1.length -ne 8) 
{
    Write-Output "Make sure you spelled your current password correctly."
    Write-Host "Please Input your" -NoNewline
    Write-Host " CURRENT PASSWORD " -ForegroundColor RED -NoNewline
    $cpassword1 = Read-Host -AsSecureString
}
$bstr = [System.Runtime.InteropServices.Marshal]::SecureStringToBSTR($cpassword1)
$cpassword = [System.Runtime.InteropServices.Marshal]::PtrToStringAuto($bstr)


$account = "(0000,0000)"

$jclfile = "$pwd\ftpjcl.txt"
$useridp = "$userid" + "P"
$useridp = $useridp.ToUpper()

del $jclfile
ac $jclfile "//$useridp JOB $account,'$userid',NOTIFY=&SYSUID,CLASS=H," 
ac $jclfile "//            MSGCLASS=H,MSGLEVEL=1"
ac $jclfile "//FOTO1A    EXEC PGM=IKJEFT01"                                                                                
ac $jclfile "//SYSTSPRT  DD SYSOUT=*,HOLD=YES"                                                          
ac $jclfile "//SYSPRINT  DD SYSOUT=*,HOLD=YES"                                     
ac $jclfile "//SYSTSIN   DD *"                                                                
ac $jclfile "  PING 8.8.8.8"      

                                       

CMD-File ($userid)

}

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


Write-Host "

**********************************************************************************************************
**********************************                                    ************************************
*********************************                 !!!!                 ***********************************
********************************                                        **********************************
*******************************                    !!                    *********************************
*******************************                   !!!!                   *********************************
*******************************                  !!!!!!                  *********************************
*******************************                 !!!!!!!!                 *********************************
*******************************                  !!!!!!                  *********************************
********************************                  !!!!                  **********************************
*********************************                  !!                  ***********************************
**********************************                                    ************************************
**********************************************************************************************************
" -ForegroundColor RED -BackgroundColor BLACK
Write-Host "

This is an FTP to JES Script

These are the LPARs available at this moment:

"

Conn-Test

Startup-PS

$selection2 = Read-Host -Prompt "If you start over, please enter YES, if not, press enter."
$selection2 = $selection2.ToUpper()
while ($selection2 -match "YES")
{
    Startup-PS
}


Write-Host "Thank you for using this FTP to JES Program."   
cmd /c 'pause'
exit