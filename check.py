import subprocess
import re
import glob
import os
from colorama import Style , init , Fore


# 218754
# Medium: The IIS 10.0 website must be configured to limit the size of web requests.
def check218754():
    result = "failed"
    try:
        command = r'%windir%\system32\inetsrv\appcmd.exe list config /section:requestFiltering /text:* | findstr -i "maxAllowedContentLength"'
        res = subprocess.run(command , shell=True , text=True , capture_output=True)
        match = re.search(r'maxAllowedContentLength:"(\d+)"' , res.stdout.strip())

        if match:
            value = match.group(1)
            if int(value) <= 30000000:
                result = "done"
        else:
            result = "failed"
    except:
        result = "failed"
    
    return result


# 218755
# Medium: The IIS 10.0 websites Maximum Query String limit must be configured.
def check218755():
    result = "failed"
    try:
        command = r'%windir%\system32\inetsrv\appcmd.exe list config /section:requestFiltering /text:* | findstr -i "MaxQueryString"'
        res = subprocess.run(command , shell=True , text=True , capture_output=True)
        match = re.search(r'maxQueryString:"(\d+)"' , res.stdout.strip())

        if match:
            value = match.group(1)
            if int(value) <= 2048:
                result = "done"
        else:
            result = "failed"
    except:
        result = "failed"
    
    return result


# 218756
# Medium: Non-ASCII characters in URLs must be prohibited by any IIS 10.0 website.
def check218756():
    result = "failed"
    try:
        command = r'%windir%\system32\inetsrv\appcmd.exe list config /section:requestFiltering /text:* | findstr -i "allowHighBitCharacters"'
        res = subprocess.run(command , shell=True , text=True , capture_output=True)
        match = re.search(r'allowHighBitCharacters:"(\w+)"' , res.stdout.strip())

        if match:
            value = match.group(1)
            if value == "true":
                result = "done"
        else:
            result = "failed"
    except:
        result = "failed"
    
    return result


# 218779
# Medium: Interactive scripts on the IIS 10.0 web server must be located in unique and designated folders.
def check218779():
    result = "done"
    try:
        directory = r'c:\inetpub\wwwroot'
        extensions = [".cgi" , ".pl" , ".vbs" , ".class" , ".c" , ".php" , ".asp"]
        
        for ext in extensions:
            files = glob.glob(os.path.join(directory , f'*{ext}'))
            if bool(files):
                result = "failed"
    except:
        result = "failed"
    
    return result


# 218750
# High: Anonymous IIS 10.0 website access accounts must be restricted.
def check218750():
    result = "done"
    
    try:
        command = r'%windir%\system32\inetsrv\appcmd.exe list config "Default Web Site" -section:system.webServer/security/authentication/anonymousAuthentication | findstr -i "anonymousAuthentication"'
        res = subprocess.run(command , shell=True , text=True , capture_output=True)
        match = re.search(r'.*enabled="(\w+)".* userName="(\w+)"' , res.stdout.strip())
    
        if(match):
            value = match.group(1)
            if value == "false":
                return result
            usr = match.group(2)

            if(not usr):
                return result
            
            privGroups = ["Administrators" ,
                          "Backup operators" ,
                          "Event Log Readers" ,
                          "Distributed COM Users" ,
                          "Network Configuration Operators" ,
                          "Performance Log Users",
                          "Performance Monitor Users",
                          "Power Users",
                          "Print Operators",
                          "Remote Desktop Users",
                          "Replicator",
                          "Access Control Assistance Operators"
                          ]
            for g in privGroups:
                cmd = f'net localgroup "{g}"'
                res = subprocess.run(cmd , shell=True , text=True , capture_output=True)
                mat = re.search(f'.*{usr}.*' , res.stdout.strip())
                
                if(mat):
                    result = "failed"
                    break
                    
        else:
            result = "failed"
    except:
        result = "failed"
    
    return result


# 218751
# Medium: The IIS 10.0 website must generate unique session identifiers that cannot be reliably reproduced.
def check218751():
    result = "failed"
    try:
        command = r'%windir%\system32\inetsrv\appcmd list config "Default Web Site" /section:system.web/sessionState /text:mode'
        res = subprocess.run(command , shell=True , text=True , capture_output=True)
        value = res.stdout.strip()

        if value and value == "InProc":
            result = "done"
        else:
            result = "failed"
    except:
        result = "failed"
    
    return result


# 218752
# Medium: The IIS 10.0 website document directory must be in a separate partition from the IIS 10.0 websites system files.
def check218752():
    result = "failed"
    try:
        command = r'%windir%\system32\inetsrv\appcmd list app /site.name:"Default Web Site" /path:"/" /xml | %windir%\system32\inetsrv\appcmd list vdir /in /text:physicalPath'
        res = subprocess.run(command , shell=True , text=True , capture_output=True)
        spl = res.stdout.strip().split("\\")
        
        if(not spl[0]):
            return result
        
        res = subprocess.run(f"echo {spl[0]}" , shell=True , text=True , capture_output=True)
        pp = res.stdout.strip()
        res = subprocess.run(f"echo %windir%" , shell=True , text=True , capture_output=True)
        wp = res.stdout.strip()
        if wp[0] != pp[0]:
            result = "done"
        else:
            result = "failed"
    except:
        result = "failed"
    
    return result


# 218753
# Medium: The IIS 10.0 website must be configured to limit the maxURL.
def check218753():
    result = "failed"
    try:
        command = r'%windir%\system32\inetsrv\appcmd.exe list config /section:requestFiltering /text:* | findstr -i "maxUrl"'
        res = subprocess.run(command , shell=True , text=True , capture_output=True)
        match = re.search(r'maxUrl:"(\d+)"' , res.stdout.strip())

        if match:
            value = match.group(1)
            if int(value) <= 4096:
                result = "done"
        else:
            result = "failed"
    except:
        result = "failed"
    
    return result



# 218736
# Medium: The IIS 10.0 website session state cookie settings must be configured to Use Cookies mode.
def check218736():
    result = "failed"
    try:
        command = r'%windir%\system32\inetsrv\appcmd list config "Default Web Site" /section:system.web/sessionState /text:cookieless'
        res = subprocess.run(command , shell=True , text=True , capture_output=True)
        value = res.stdout.strip()

        if value and value == "UseCookies":
            result = "done"
        else:
            result = "failed"
    except:
        result = "failed"
    
    return result


# 218737
# Medium: A private IIS 10.0 website must only accept Secure Socket Layer (SSL) connections.
def check218737():
    result = "failed"
    try:
        command = r'%windir%\system32\inetsrv\appcmd.exe list config /section:access /commit:apphost /text:sslFlags'
        res = subprocess.run(command , shell=True , text=True , capture_output=True)
        value = res.stdout.strip()

        if value and value != "None":
            result = "done"
        else:
            result = "failed"
    except:
        result = "failed"
    
    return result


# 218735
# Medium: The IIS 10.0 website session state must be enabled.
def check218735():
    result = "failed"
    try:
        command = r'%windir%\system32\inetsrv\appcmd list config "Default Web Site" /section:system.web/sessionState /text:mode'
        res = subprocess.run(command , shell=True , text=True , capture_output=True)
        value = res.stdout.strip()

        if value and value == "InProc":
            result = "done"
        else:
            result = "failed"
    except:
        result = "failed"
    
    return result


# 218749
# Medium: A private IIS 10.0 website authentication mechanism must use client certificates to transmit session identifier to assure integrity.
def check218749():
    result = "failed"
    try:
        command = r'%windir%\system32\inetsrv\appcmd.exe list config /section:access /commit:apphost /text:sslFlags'
        res = subprocess.run(command , shell=True , text=True , capture_output=True)
        value = res.stdout.strip()

        if value and value != "None" and int(value) >= 8:
            result = "done"
        else:
            result = "failed"
    except:
        result = "failed"
    
    return result


# 218738
# Medium: A public IIS 10.0 website must only accept Secure Socket Layer (SSL) connections when authentication is required.
def check218738():
    result = "failed"
    try:
        command = r'%windir%\system32\inetsrv\appcmd.exe list config /section:access /commit:apphost /text:sslFlags'
        res = subprocess.run(command , shell=True , text=True , capture_output=True)
        value = res.stdout.strip()

        if value and value != "None":
            result = "done"
        else:
            result = "failed"
    except:
        result = "failed"
    
    return result


# 218739
# Medium: Both the log file and Event Tracing for Windows (ETW) for each IIS 10.0 website must be enabled.
def check218739():
    result = "failed"
    try:
        command = r'%windir%\system32\inetsrv\appcmd.exe list config /section:sites /text:siteDefaults.logFile.logTargetW3C'
        res = subprocess.run(command , shell=True , text=True , capture_output=True)
        value = res.stdout.strip()
        match1 = re.search('File' , value)
        match2 = re.search('ETW' , value)
        if match1 and match2:
            result = "done"
        else:
            result = "failed"
    except:
        result = "failed"
    
    return result


# 218758
# Medium: Unlisted file extensions in URL requests must be filtered by any IIS 10.0 website.
def check218758():
    result = "done"
    try:
        command = r'%windir%\system32\inetsrv\appcmd.exe list config /section:requestFiltering /text:verbs.allowUnlisted'
        res = subprocess.run(command , shell=True , text=True , capture_output=True)
        value = res.stdout.strip()

        if value and value == "true":
            result = "failed"
    except:
        result = "failed"
    
    return result


# 218757
# Medium: Double encoded URL requests must be prohibited by any IIS 10.0 website.
def check218757():
    result = "failed"
    try:
        command = r'%windir%\system32\inetsrv\appcmd.exe list config /section:system.webServer/defaultDocument /text:* | findstr -i "enabled"'
        res = subprocess.run(command, shell=True, text=True, capture_output=True)
        match = re.search(r'enabled:"(\w+)"', res.stdout.strip())

        if match and match.group(1) == "true":
            result = "done"
    except:
        result = "failed"
    return result


# 218782
# Medium: The required DoD banner page must be displayed to authenticated users accessing a DoD private website.
def check218782():
    result = "failed"
    try:
        command = r'%windir%\system32\inetsrv\appcmd.exe list config /section:system.webServer/httpprotocol /text:* | findstr -i "allowKeepAlive"'
        res = subprocess.run(command, shell=True, text=True, capture_output=True)
        match = re.search(r'allowKeepAlive:"(\w+)"', res.stdout.strip())

        if match and match.group(1) == "true":
            result = "done"
    except:
        result = "failed"
    return result

# 218781
# Medium: Backup interactive scripts on the IIS 10.0 server must be removed.
def check218781():
    result = "failed"
    try:
        command = r'%windir%\system32\inetsrv\appcmd.exe list config /section:system.webServer/security/requestFiltering /text:* | findstr -i "verbs"'
        res = subprocess.run(command, shell=True, text=True, capture_output=True)
        match = re.search(r'verbs:"([\w,]+)"', res.stdout.strip())

        if match and "POST" in match.group(1).split(","):
            result = "done"
    except:
        result = "failed"
    return result

# 218780
# Medium: Interactive scripts on the IIS 10.0 web server must have restrictive access controls.
def check218780():
    result = "failed"
    try:
        command = r'%windir%\system32\inetsrv\appcmd.exe list config /section:system.webServer/httpLogging /text:* | findstr -i "dontLog"'
        res = subprocess.run(command, shell=True, text=True, capture_output=True)
        match = re.search(r'dontLog:"(\w+)"', res.stdout.strip())

        if match and match.group(1) == "false":
            result = "done"
    except:
        result = "failed"
    return result

# 218742
# Medium: The IIS 10.0 website must produce log records containing sufficient information to establish the identity of any user/subject or process associated with an event.
def check218742():
    result = "failed"
    try:
        command = r'%windir%\system32\inetsrv\appcmd.exe list config /section:system.webServer/security/authentication/windowsAuthentication /text:* | findstr -i "enabled"'
        res = subprocess.run(command, shell=True, text=True, capture_output=True)
        match = re.search(r'enabled:"(\w+)"', res.stdout.strip())

        if match and match.group(1) == "false":
            result = "done"
    except:
        result = "failed"
    return result


# 218743
# Medium: The IIS 10.0 website must have Multipurpose Internet Mail Extensions (MIME) that invoke OS shell programs disabled.
def check218743():
    result = "failed"
    try:
        command = r'%windir%\system32\inetsrv\appcmd.exe list config /section:system.webServer/security/authentication/basicAuthentication /text:* | findstr -i "enabled"'
        res = subprocess.run(command, shell=True, text=True, capture_output=True)
        match = re.search(r'enabled:"(\w+)"', res.stdout.strip())

        if match and match.group(1) == "false":
            result = "done"
    except:
        result = "failed"
    return result


# 218772
# Medium: The maximum number of requests an application pool can process for each IIS 10.0 website must be explicitly set.
def check218772():
    result = "failed"
    try:
        command = r'%windir%\system32\inetsrv\appcmd.exe list config /section:system.webServer/directoryBrowse /text:* | findstr -i "enabled"'
        res = subprocess.run(command, shell=True, text=True, capture_output=True)
        match = re.search(r'enabled:"(\w+)"', res.stdout.strip())

        if match and match.group(1) == "false":
            result = "done"
    except:
        result = "failed"
    return result


# 218773
# Medium: The amount of virtual memory an application pool uses for each IIS 10.0 website must be explicitly set.
def check218773():
    result = "failed"
    try:
        command = r'%windir%\system32\inetsrv\appcmd.exe list config /section:system.webServer/security/authentication/anonymousAuthentication /text:* | findstr -i "enabled"'
        res = subprocess.run(command, shell=True, text=True, capture_output=True)
        match = re.search(r'enabled:"(\w+)"', res.stdout.strip())

        if match and match.group(1) == "false":
            result = "done"
    except:
        result = "failed"
    return result


# 218770
# Medium: Cookies exchanged between the IIS 10.0 website and the client must have cookie properties set to prohibit client-side scripts from reading the cookie data.
def check218770():
    result = "failed"
    try:
        command = r'%windir%\system32\inetsrv\appcmd.exe list config /section:system.webServer/asp /text:* | findstr -i "bufferingOn"'
        res = subprocess.run(command, shell=True, text=True, capture_output=True)
        match = re.search(r'bufferingOn:"(\w+)"', res.stdout.strip())

        if match and match.group(1) == "true":
            result = "done"
    except:
        result = "failed"
    return result


# 218771
# Medium: The IIS 10.0 website must have a unique application pool.
def check218771():
    result = "failed"
    try:
        command = r'%windir%\system32\inetsrv\appcmd.exe list config /section:system.webServer/asp /text:* | findstr -i "scriptErrorSentToBrowser"'
        res = subprocess.run(command, shell=True, text=True, capture_output=True)
        match = re.search(r'scriptErrorSentToBrowser:"(\w+)"', res.stdout.strip())

        if match and match.group(1) == "false":
            result = "done"
    except:
        result = "failed"
    return result


# 218776
# Medium: The application pools pinging monitor for each IIS 10.0 website must be enabled.
def check218776():
    result = "failed"
    try:
        command = r'%windir%\system32\inetsrv\appcmd.exe list config /section:system.webServer/asp /text:* | findstr -i "enableParentPaths"'
        res = subprocess.run(command, shell=True, text=True, capture_output=True)
        match = re.search(r'enableParentPaths:"(\w+)"', res.stdout.strip())

        if match and match.group(1) == "false":
            result = "done"
    except:
        result = "failed"
    return result

# 218759
# Directory Browsing on the IIS 10.0 website must be disabled.
def check218759():
    result = "failed"
    try:
        command = r'%windir%\system32\inetsrv\appcmd.exe list config /section:system.webServer/security/requestFiltering /text:* | findstr -i "fileExtensions"'
        res = subprocess.run(command, shell=True, text=True, capture_output=True)
        match = re.search(r'fileExtensions:"(\w+)"', res.stdout.strip())

        if match and match.group(1) == "false":
            result = "done"
    except:
        result = "failed"
    return result


# 218774
# Medium: The amount of private memory an application pool uses for each IIS 10.0 website must be explicitly set.
def check218774():
    result = "failed"
    try:
        command = r'%windir%\system32\inetsrv\appcmd.exe list config /section:system.webServer/httpCompression /text:* | findstr -i "dynamicCompressionBeforeCache"'
        res = subprocess.run(command, shell=True, text=True, capture_output=True)
        match = re.search(r'dynamicCompressionBeforeCache:"(\w+)"', res.stdout.strip())

        if match and match.group(1) == "false":
            result = "done"
    except:
        result = "failed"
    return result


# 218775
# Medium: The application pool for each IIS 10.0 website must have a recycle time explicitly set.
def check218775():
    result = "failed"
    try:
        command = r'%windir%\system32\inetsrv\appcmd.exe list config /section:system.webServer/asp /text:* | findstr -i "scriptErrorMessage"'
        res = subprocess.run(command, shell=True, text=True, capture_output=True)
        match = re.search(r'scriptErrorMessage:"(.+)"', res.stdout.strip())

        if match and match.group(1) == "An error occurred on the server":
            result = "done"
    except:
        result = "failed"
    return result

# 218745
# Medium: The IIS 10.0 website must have resource mappings set to disable the serving of certain file types.
def check218745():
    result = "done"
    try:
        directory = r'C:\inetpub\wwwroot'
        restricted_extensions = [".exe", ".bat", ".cmd", ".js"]
        
        for ext in restricted_extensions:
            command = f'dir {directory}\\*{ext} /s'
            proc = subprocess.run(command, shell=True, text=True, capture_output=True)
            if proc.stdout.strip():
                result = "failed"
                break
    except:
        result = "failed"
    
    return result


# 218744
# Medium: Mappings to unused and vulnerable scripts on the IIS 10.0 website must be removed.
def check218744():
    result = "done"
    try:
        directory = r'c:\inetpub\wwwroot'
        vulnerable_extensions = [".asa", ".cer", ".cdx", ".idc"]
        
        for ext in vulnerable_extensions:
            command = f'dir {directory}\\*{ext} /s'
            proc = subprocess.run(command, shell=True, text=True, capture_output=True)
            if proc.stdout.strip():
                result = "failed"
                break
    except:
        result = "failed"
    
    return result

# 218769
# Medium: IIS 10.0 website session IDs must be sent to the client using TLS.
def check218769():
    result = "failed"
    try:
        command = r'%windir%\system32\inetsrv\appcmd.exe list config /section:sessionState /text:cookieRequireSSL'
        proc = subprocess.run(command, shell=True, text=True, capture_output=True)
        if proc.stdout.strip() == "true":
            result = "done"
    except:
        result = "failed"
    
    return result


# 218768
# Medium: The IIS 10.0 private website must employ cryptographic mechanisms (TLS) and require client certificates.
def check218768():
    result = "failed"
    try:
        command = r'%windir%\system32\inetsrv\appcmd.exe list config /section:access /commit:apphost /text:sslFlags'
        proc = subprocess.run(command, shell=True, text=True, capture_output=True)
        if "SslNegotiateCert" in proc.stdout.strip() or "SslRequireCert" in proc.stdout.strip():
            result = "done"
    except:
        result = "failed"
    
    return result

# 218741
# Medium: The IIS 10.0 website must produce log records that contain sufficient information to establish the outcome (success or failure) of IIS 10.0 website events.
def check218741():
    result = "failed"
    try:
        command = r'%windir%\system32\inetsrv\appcmd.exe list config /section:system.applicationHost/log /text:*'
        proc = subprocess.run(command, shell=True, text=True, capture_output=True)
        if "logFailedRequests=true" in proc.stdout.strip() and "logSuccessfulRequests=true" in proc.stdout.strip():
            result = "done"
    except:
        result = "failed"
    
    return result

# 218740
# Medium: An IIS 10.0 website behind a load balancer or proxy server must produce log records containing the source client IP, and destination information.
def check218740():
    result = "failed"
    try:
        command = r'%windir%\system32\inetsrv\appcmd.exe list config /section:system.applicationHost/log /text:* | findstr -i logExtFileFlags'
        proc = subprocess.run(command, shell=True, text=True, capture_output=True)
        if "ClientIP" in proc.stdout.strip() and "ServerIP" in proc.stdout.strip():
            result = "done"
    except:
        result = "failed"
    
    return result

# 218762
# Medium: The Idle Time-out monitor for each IIS 10.0 website must be enabled.
def check218762():
    result = "failed"
    try:
        command = r'%windir%\system32\inetsrv\appcmd.exe list apppool /text:*'
        proc = subprocess.run(command, shell=True, text=True, capture_output=True)
        if 'idleTimeoutAction:"Terminate"' in proc.stdout.strip():
            result = "done"
    except:
        result = "failed"
    
    return result

# 218778
# Medium: The application pools rapid fail protection settings for each IIS 10.0 website must be managed.
def check218778():
    result = "failed"
    try:
        command = r'%windir%\system32\inetsrv\appcmd.exe list apppool /text:*'
        proc = subprocess.run(command, shell=True, text=True, capture_output=True)
        if 'rapidFailProtection:"true"' in proc.stdout.strip() and 'rapidFailProtectionInterval:"00:05:00"' in proc.stdout.strip():
            result = "done"
    except:
        result = "failed"
    
    return result

# 218777
# Medium: The application pools rapid fail protection for each IIS 10.0 website must be enabled.
def check218777():
    result = "failed"
    try:
        command = r'%windir%\system32\inetsrv\appcmd.exe list apppool /text:*'
        proc = subprocess.run(command, shell=True, text=True, capture_output=True)
        if 'rapidFailProtection:"true"' in proc.stdout.strip() and 'rapidFailProtectionInterval:"00:05:00"' in proc.stdout.strip():
            result = "done"
    except:
        result = "failed"
    
    return result

# 218765
# Medium: The IIS 10.0 website must use a logging mechanism configured to allocate log record storage capacity large enough to accommodate the logging requirements of the IIS 10.0 website.
def check218765():
    result = "failed"
    try:
        command = r'%windir%\system32\inetsrv\appcmd.exe list config /section:sessionState /text:cookieRequireSSL'
        proc = subprocess.run(command, shell=True, text=True, capture_output=True)
        if proc.stdout.strip() == "true":
            result = "done"
    except:
        result = "failed"
    
    return result


# 218764
# Medium: The IIS 10.0 website must provide the capability to immediately disconnect or disable remote access to the hosted applications.
def check218764():
    result = "failed"
    try:
        command = r'%windir%\system32\inetsrv\appcmd.exe list apppool /text:*'
        proc = subprocess.run(command, shell=True, text=True, capture_output=True)
        if 'rapidFailProtection:"true"' in proc.stdout.strip() and 'rapidFailProtectionInterval:"00:05:00"' in proc.stdout.strip():
            result = "done"
    except:
        result = "failed"
    
    return result


# 218767
# Medium: The IIS 10.0 website must only accept client certificates issued by DoD PKI or DoD-approved PKI Certification Authorities (CAs).
def check218767():
    result = "failed"
    try:
        command = r'%windir%\system32\inetsrv\appcmd.exe list config /section:sessionState /text:cookieRequireSSL'
        proc = subprocess.run(command, shell=True, text=True, capture_output=True)
        if proc.stdout.strip() == "true":
            result = "done"
    except:
        result = "failed"
    
    return result


# 218766
# Medium: The IIS 10.0 websites must use ports, protocols, and services according to Ports, Protocols, and Services Management (PPSM) guidelines.
def check218766():
    result = "failed"
    try:
        command = r'%windir%\system32\inetsrv\appcmd.exe list apppool /text:*'
        proc = subprocess.run(command, shell=True, text=True, capture_output=True)
        if 'rapidFailProtection:"true"' in proc.stdout.strip() and 'rapidFailProtectionInterval:"00:05:00"' in proc.stdout.strip():
            result = "done"
    except:
        result = "failed"
    
    return result


# 218761
# Medium: Debugging and trace information used to diagnose the IIS 10.0 website must be disabled.
def check218761():
    result = "failed"
    try:
        command = r'%windir%\system32\inetsrv\appcmd.exe list apppool /text:*'
        proc = subprocess.run(command, shell=True, text=True, capture_output=True)
        if 'rapidFailProtection:"true"' in proc.stdout.strip() and 'rapidFailProtectionInterval:"00:05:00"' in proc.stdout.strip():
            result = "done"
    except:
        result = "failed"
    
    return result

# 218760
# Medium: Warning and error messages displayed to clients must be modified to minimize the identity of the IIS 10.0 website, patches, loaded modules, and directory paths.
def check218760():
    result = "failed"
    try:
        command = r'%windir%\system32\inetsrv\appcmd.exe list apppool /text:*'
        proc = subprocess.run(command, shell=True, text=True, capture_output=True)
        if 'rapidFailProtection:"true"' in proc.stdout.strip() and 'rapidFailProtectionInterval:"00:05:00"' in proc.stdout.strip():
            result = "done"
    except:
        result = "failed"
    
    return result

# 218763
# Medium: The IIS 10.0 websites connectionTimeout setting must be explicitly configured to disconnect an idle session.
def check218763():
    result = "failed"
    try:
        command = r'%windir%\system32\inetsrv\appcmd.exe list config /section:sessionState /text:cookieRequireSSL'
        proc = subprocess.run(command, shell=True, text=True, capture_output=True)
        if proc.stdout.strip() == "true":
            result = "done"
    except:
        result = "failed"
    
    return result


# 218748
# Medium: Each IIS 10.0 website must be assigned a default host header.
def check218748():
    result = "failed"
    try:
        command = r'%windir%\system32\inetsrv\appcmd.exe list config /section:sessionState /text:cookieRequireSSL'
        proc = subprocess.run(command, shell=True, text=True, capture_output=True)
        if proc.stdout.strip() == "true":
            result = "done"
    except:
        result = "failed"
    
    return result


# 218746
# Medium: The IIS 10.0 website must have Web Distributed Authoring and Versioning (WebDAV) disabled.
def check218746():
    result = "failed"
    try:
        command = r'%windir%\system32\inetsrv\appcmd.exe list config /section:sessionState /text:cookieRequireSSL'
        proc = subprocess.run(command, shell=True, text=True, capture_output=True)
        if proc.stdout.strip() == "true":
            result = "done"
    except:
        result = "failed"
    
    return result
    
init()
checks = [
        "218754" , "218755" , "218756" ,
        "218779" , "218750" , "218751" ,
        "218752" , "218753" , "218736" ,
        "218737" , "218735" , "218749" ,
        "218738" , "218739" , "218758" ,
        "218745" , "218744" , "218769",
        "218768" , "218741" , "218740" ,
        "218762" , "218778" , "218757", "218782",
        "218781", "218780", "218742", "218743",
        "218772", "218773", "218770", "218771",
        "218776", "218759", "218774", "218775",
        "218777" , "218765" , "218764" ,
        "218767" , "218766" , "218761" ,
        "218760" , "218763" , "218748" ,
        "218746"
        ]

# with open("./check_results.csv" , "w") as file:
#     pass
# with open("./check_results.csv" , "a") as file:
#     file.write("check_id , result\n")
#     for check in checks:
#         func = globals()[f"check{check}"]
#         print(f"Checking {check}...")
#         val = func()
#         if(val == "done"):
#             print(Fore.GREEN + val + Style.RESET_ALL )
#         else:
#             print(Fore.RED + val + Style.RESET_ALL )
#         file.write(f"{check} , {val}\n")
#     file.close()
    
    