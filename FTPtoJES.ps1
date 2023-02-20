

$pwd = ([Environment]::GetFolderPath("Desktop") + "\FTPtoJES")

if (Test-Path $pwd -ErrorAction SilentlyContinue) {
  $null
}
else
{
New-Item ([Environment]::GetFolderPath("Desktop") + "\FTPtoJES") -Type Directory > $null
}

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------



Function Quick-Run {

Write-Host "Please enter your JOBCARD in the TEXT file. When done, press enter."
notepad.exe $pwd\jobcard.txt

cmd /c 'pause'

Write-Host "Please enter your JCL STEPS in the TEXT file. When done, press enter."
notepad.exe $pwd\jclsteps.txt

cmd /c 'pause'

gc $pwd\jobcard.txt,$pwd\jclsteps.txt > $pwd\jcltosub.txt

$hostname = Read-Host -Prompt 'Input your hostname'

Conn-Test


$ftptype = Write-Host -Prompt 'Input the type of FTP transmission you will use for the connection to $hostname :'


Write-Host "To use " -NoNewline
Write-Host "ACTIVE FTP" -ForegroundColor RED -NoNewline
Write-Host ", enter " -NoNewline
Write-Host "ACTIVE" -ForegroundColor RED

Write-Host "To use " -NoNewline
Write-Host "PASSIVE FTP" -ForegroundColor GREEN -NoNewline
Write-Host ", enter " -NoNewline
Write-Host "PASSIVE" -ForegroundColor GREEN

Write-Host "To use " -NoNewline
Write-Host "FTP with TLS" -ForegroundColor YELLOW -NoNewline
Write-Host ", enter " -NoNewline
Write-Host "FTPS" -ForegroundColor YELLOW -NoNewline
Write-Host " - This option only supports PASSIVE FTP."

$selection4 = Read-Host -Prompt "Please enter your selection (ACTIVE, PASSIVE, FTPS)"
$selection4 = $selection4.ToUpper()

Write-Host "
You will now submit a JCL in: $hostname
"

if ($selection4 -match "ACTIVE")
{
Active-FTP 
}
elseif ($selection4 -match "PASSIVE")
{
Passive-FTP > $null
}
elseif ($selection4 -match "FTPS")
{
Passive-FTPS > $null
}

}

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Function Active-FTP ($userid) {

$userid = Read-Host -Prompt "Please enter your USERID"

Write-Host "
The Password rules for the Mainframe only allow 8-character-long passwords.

The password can only be entered in Alphanumeric characters (letters and numbers).

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
lcd $pwd     
put jcltosub.txt
mget *
exit
" | ftp -i -n -d
}

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


Function Passive-FTP ($userid) {

$userid = Read-Host -Prompt "Please enter your USERID"

Write-Host "
The Password rules for the Mainframe only allow 8-character-long passwords.

The password can only be entered in Alphanumeric characters (letters and numbers).

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

    & 'C:\Program Files (x86)\WinSCP\WinSCP.com' `
      /log="$pwd\WinSCP.log" /ini=nul `
      /command `
        "open -passive=on ftp://${userid}:$cpassword@$hostname/" `
        "call site file=jes NOJESGETBYDSN" `
        "ascii" `
        "lcd $pwd" `
        "put ftptosub.txt" `
        "exit"
    }

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


Function Passive-FTPS ($userid) {

$userid = Read-Host -Prompt "Please enter your USERID"

Write-Host "
The Password rules for the Mainframe only allow 8-character-long passwords.

The password can only be entered in Alphanumeric characters (letters and numbers).

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

    & 'C:\Program Files (x86)\WinSCP\WinSCP.com' `
      /log="$pwd\WinSCP.log" /ini=nul `
      /command `
        "open -passive=off ftpes://${userid}:$cpassword@$hostname/" `
        "call site file=jes NOJESGETBYDSN" `
        "ascii" `
        "lcd $pwd" `
        "put ftptosub.txt" `
        "exit"
        "exit"
    }

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


Function Conn-Test {

$pingresult = Test-Connection -ComputerName $hostname -Count 1 -ErrorAction SilentlyContinue
    if ( $pingresult -ne $NULL )
    {
		Write-Host "$hostname is Online" -ForegroundColor Green
    }
    else 
    {
        Write-Host "$hostname is NOT ONLINE" -ForegroundColor Red
    }
    
}

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


# -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


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

"

Quick-Run

$selection2 = Read-Host -Prompt "If you start over, please enter YES, if not, press enter."
$selection2 = $selection2.ToUpper()
while ($selection2 -match "YES")
{
    Quick-Run
}


Write-Host "Thank you for using this FTP to JES Program."   
cmd /c 'pause'
exit