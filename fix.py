import subprocess
from colorama import Style , init , Fore

# 218754
# Medium: The IIS 10.0 website must be configured to limit the size of web requests.
def fix218754():
    result = "undone"
    try:
        command = r'%windir%\system32\inetsrv\appcmd.exe set config /section:requestFiltering /requestLimits.maxAllowedContentLength:30000000'
        res = subprocess.run(command , shell=True , text=True , capture_output=True)

        if "Applied" in res.stdout.strip():
            result = "done"
        else:
            result = "undone"
    except:
        result = "undone"
    
    return result


# 218755
# Medium: The IIS 10.0 websites Maximum Query String limit must be configured.
def fix218755():
    result = "undone"
    try:
        command = r'%windir%\system32\inetsrv\appcmd.exe set config /section:requestFiltering /requestLimits.maxQueryString:2048'
        res = subprocess.run(command , shell=True , text=True , capture_output=True)

        if "Applied" in res.stdout.strip():
            result = "done"
        else:
            result = "undone"
    except:
        result = "undone"
    
    return result


# 218756
# Medium: Non-ASCII characters in URLs must be prohibited by any IIS 10.0 website.
def fix218756():
    result = "undone"
    try:
        command = r'%windir%\system32\inetsrv\appcmd.exe set config /section:requestFiltering /allowHighBitCharacters:false'
        res = subprocess.run(command , shell=True , text=True , capture_output=True)

        if "Applied" in res.stdout.strip():
            result = "done"
        else:
            result = "undone"
    except:
        result = "undone"
    
    return result

# 218779
# Medium: Interactive scripts on the IIS 10.0 web server must be located in unique and designated folders.
def fix218779():
    result = "undone(can't be done with script)"
    
    return result

# 218750
# High: Anonymous IIS 10.0 website access accounts must be restricted.
def fix218750():
    result = "undone"
    
    try:
        command = r'%windir%\system32\inetsrv\appcmd.exe set config -section:system.webServer/security/authentication/anonymousAuthentication /enabled:false'
        res = subprocess.run(command , shell=True , text=True , capture_output=True)
    
        if "Applied" in res.stdout.strip():
            result = "done"
                    
        else:
            result = "undone"
    except:
        result = "undone"
    
    return result


# 218751
# Medium: The IIS 10.0 website must generate unique session identifiers that cannot be reliably reproduced.
def fix218751():
    result = "undone"
    try:
        command = r'%windir%\system32\inetsrv\appcmd set config /section:system.web/sessionState /mode:InProc'
        res = subprocess.run(command , shell=True , text=True , capture_output=True)

        if "Applied" in res.stdout.strip():
            result = "done"
        else:
            result = "undone"
    except:
        result = "undone"
    
    return result

# 218752
# Medium: The IIS 10.0 website document directory must be in a separate partition from the IIS 10.0 websites system files.
def fix218752():
    result = "undone(can't be done with script)"
    
    return result

# 218753
# Medium: The IIS 10.0 website must be configured to limit the maxURL.
def fix218753():
    result = "undone"
    try:
        command = r'%windir%\system32\inetsrv\appcmd.exe set config /section:requestFiltering /requestLimits.maxUrl:4096'
        res = subprocess.run(command , shell=True , text=True , capture_output=True)

        if "Applied" in res.stdout.strip():
            result = "done"
        else:
            result = "undone"
    except:
        result = "undone"
    
    return result


# 218736
# Medium: The IIS 10.0 website session state cookie settings must be configured to Use Cookies mode.
def fix218736():
    result = "undone"
    try:
        command = r'%windir%\system32\inetsrv\appcmd set config /section:system.web/sessionState /cookieless:UseCookies'
        res = subprocess.run(command , shell=True , text=True , capture_output=True)

        if "Applied" in res.stdout.strip():
            result = "done"
        else:
            result = "undone"
    except:
        result = "undone"
    
    return result


# 218737
# Medium: A private IIS 10.0 website must only accept Secure Socket Layer (SSL) connections.
def fix218737():
    result = "undone"
    try:
        command = r'%windir%\system32\inetsrv\appcmd.exe set config /section:access /sslFlags:SslRequireCert'
        res = subprocess.run(command , shell=True , text=True , capture_output=True)

        if "Applied" in res.stdout.strip():
            result = "done"
        else:
            result = "undone"
    except:
        result = "undone"
    
    return result


# 218735
# Medium: The IIS 10.0 website session state must be enabled.
def fix218735():
    result = "undone"
    try:
        command = r'%windir%\system32\inetsrv\appcmd set config /section:system.web/sessionState /mode:InProc'
        res = subprocess.run(command , shell=True , text=True , capture_output=True)

        if "Applied" in res.stdout.strip():
            result = "done"
        else:
            result = "undone"
    except:
        result = "undone"
    
    return result


# 218749
# Medium: A private IIS 10.0 website authentication mechanism must use client certificates to transmit session identifier to assure integrity.
def fix218749():
    result = "undone"
    try:
        command = r'%windir%\system32\inetsrv\appcmd.exe set config /section:access /sslFlags:SslRequireCert'
        res = subprocess.run(command , shell=True , text=True , capture_output=True)

        if "Applied" in res.stdout.strip():
            result = "done"
        else:
            result = "undone"
    except:
        result = "undone"
    
    return result


# 218738
# Medium: A public IIS 10.0 website must only accept Secure Socket Layer (SSL) connections when authentication is required.
def fix218738():
    result = "undone"
    try:
        command = r'%windir%\system32\inetsrv\appcmd.exe set config /section:access /sslFlags:SslRequireCert'
        res = subprocess.run(command , shell=True , text=True , capture_output=True)

        if "Applied" in res.stdout.strip():
            result = "done"
        else:
            result = "undone"
    except:
        result = "undone"
    
    return result


# 218739
# Medium: Both the log file and Event Tracing for Windows (ETW) for each IIS 10.0 website must be enabled.
def fix218739():
    result = "undone"
    try:
        command = r'%windir%\system32\inetsrv\appcmd.exe set config /section:sites /siteDefaults.logFile.logTargetW3C:File,ETW'
        res = subprocess.run(command , shell=True , text=True , capture_output=True)
        if "Applied" in res.stdout.strip():
            result = "done"
        else:
            result = "undone"
    except:
        result = "undone"
    
    return result


# 218758
# Medium: Unlisted file extensions in URL requests must be filtered by any IIS 10.0 website.
def fix218758():
    result = "undone"
    try:
        command = r'%windir%\system32\inetsrv\appcmd.exe set config /section:requestFiltering /verbs.allowUnlisted:false'
        res = subprocess.run(command , shell=True , text=True , capture_output=True)

        if "Applied" in res.stdout.strip():
            result = "done"
    except:
        result = "undone"
    
    return result

# 218745
# Medium: The IIS 10.0 website must have resource mappings set to disable the serving of certain file types.
def fix218745():
    result = "undone"
    try:
        command = r'%windir%\system32\inetsrv\appcmd.exe set config /section:staticContent /remove'
        res = subprocess.run(command, shell=True, text=True, capture_output=True)
        if "Applied" in res.stdout.strip():
            result = "done"
    except:
        result = "undone"
    return result


# 218744
# Medium: Mappings to unused and vulnerable scripts on the IIS 10.0 website must be removed.
def fix218744():
    result = "undone"
    try:
        command = r'%windir%\system32\inetsrv\appcmd.exe set config /section:staticContent /remove'
        res = subprocess.run(command, shell=True, text=True, capture_output=True)
        if "Applied" in res.stdout.strip():
            result = "done"
    except:
        result = "undone"
    return result


# 218769
# Medium: IIS 10.0 website session IDs must be sent to the client using TLS.
def fix218769():
    result = "undone"
    try:
        command = r'%windir%\system32\inetsrv\appcmd.exe set config /section:access /sslFlags:Ssl'
        res = subprocess.run(command, shell=True, text=True, capture_output=True)
        if "Applied" in res.stdout.strip():
            result = "done"
    except:
        result = "undone"
    return result


# 218768
# Medium: The IIS 10.0 private website must employ cryptographic mechanisms (TLS) and require client certificates.
def fix218768():
    result = "undone"
    try:
        command = r'%windir%\system32\inetsrv\appcmd.exe set config /section:access /sslFlags:SslNegotiateCert'
        res = subprocess.run(command, shell=True, text=True, capture_output=True)
        if "Applied" in res.stdout.strip():
            result = "done"
    except:
        result = "undone"
    return result


# 218741
# Medium: The IIS 10.0 website must produce log records that contain sufficient information to establish the outcome (success or failure) of IIS 10.0 website events.
def fix218741():
    result = "undone"
    try:
        command = r'%windir%\system32\inetsrv\appcmd.exe set config /section:system.webServer/httpLogging /logFile.customFields:+x-forwarded-for'
        res = subprocess.run(command, shell=True, text=True, capture_output=True)
        if "Applied" in res.stdout.strip():
            result = "done"
    except:
        result = "undone"
    return result


# 218740
# Medium: An IIS 10.0 website behind a load balancer or proxy server must produce log records containing the source client IP, and destination information.
def fix218740():
    result = "undone"
    try:
        command = r'%windir%\system32\inetsrv\appcmd.exe set config /section:system.webServer/httpLogging /logFile.customFields:+x-forwarded-for'
        res = subprocess.run(command, shell=True, text=True, capture_output=True)
        if "Applied" in res.stdout.strip():
            result = "done"
    except:
        result = "undone"
    return result


# 218762
# Medium: The Idle Time-out monitor for each IIS 10.0 website must be enabled.
def fix218762():
    result = "undone"
    try:
        command = r'%windir%\system32\inetsrv\appcmd.exe set config /section:system.applicationHost/applicationPools /[name=\'DefaultAppPool\'].processModel.idleTimeout:20:00:00'
        res = subprocess.run(command, shell=True, text=True, capture_output=True)
        if "Applied" in res.stdout.strip():
            result = "done"
    except:
        result = "undone"
    return result


# 218778
# Medium: The application pools rapid fail protection settings for each IIS 10.0 website must be managed.
def fix218778():
    result = "undone"
    try:
        command = r'%windir%\system32\inetsrv\appcmd.exe set config /section:system.applicationHost/applicationPools /[name=\'DefaultAppPool\'].failure.rapidFailProtection:true'
        res = subprocess.run(command, shell=True, text=True, capture_output=True)
        if "Applied" in res.stdout.strip():
            result = "done"
    except:
        result = "undone"
    return result


# 218757
# Medium: Double encoded URL requests must be prohibited by any IIS 10.0 website.
def fix218757():
    result = "undone"
    try:
        command = r'%windir%\system32\inetsrv\appcmd.exe set config /section:requestFiltering /requestLimits.maxAllowedContentLength:30000000'
        res = subprocess.run(command , shell=True , text=True , capture_output=True)

        if "Applied" in res.stdout.strip():
            result = "done"
        else:
            result = "undone"
    except:
        result = "undone"
    
    return result


# 218782
# Medium: The required DoD banner page must be displayed to authenticated users accessing a DoD private website.
def fix218782():
    result = "undone"
    try:
        command = r'%windir%\system32\inetsrv\appcmd.exe set config /section:requestFiltering /requestLimits.maxQueryString:2048'
        res = subprocess.run(command , shell=True , text=True , capture_output=True)

        if "Applied" in res.stdout.strip():
            result = "done"
        else:
            result = "undone"
    except:
        result = "undone"
    
    return result


# 218781
# Medium: Backup interactive scripts on the IIS 10.0 server must be removed.
def fix218781():
    result = "undone"
    try:
        command = r'%windir%\system32\inetsrv\appcmd.exe set config /section:requestFiltering /allowHighBitCharacters:false'
        res = subprocess.run(command , shell=True , text=True , capture_output=True)

        if "Applied" in res.stdout.strip():
            result = "done"
        else:
            result = "undone"
    except:
        result = "undone"
    
    return result


# 218780
# Medium: Interactive scripts on the IIS 10.0 web server must have restrictive access controls.
def fix218780():
    result = "undone(can't be done with script)"
    
    return result

# 218742
# Medium: The IIS 10.0 website must produce log records containing sufficient information to establish the identity of any user/subject or process associated with an event.
def fix218742():
    result = "undone"
    
    try:
        command = r'%windir%\system32\inetsrv\appcmd.exe set config -section:system.webServer/security/authentication/anonymousAuthentication /enabled:false'
        res = subprocess.run(command , shell=True , text=True , capture_output=True)
    
        if "Applied" in res.stdout.strip():
            result = "done"
                    
        else:
            result = "undone"
    except:
        result = "undone"
    
    return result


# 218743
# Medium: The IIS 10.0 website must have Multipurpose Internet Mail Extensions (MIME) that invoke OS shell programs disabled.
def fix218743():
    result = "undone"
    try:
        command = r'%windir%\system32\inetsrv\appcmd set config /section:system.web/sessionState /mode:InProc'
        res = subprocess.run(command , shell=True , text=True , capture_output=True)

        if "Applied" in res.stdout.strip():
            result = "done"
        else:
            result = "undone"
    except:
        result = "undone"
    
    return result

# 218770
# Medium: Cookies exchanged between the IIS 10.0 website and the client must have cookie properties set to prohibit client-side scripts from reading the cookie data.
def fix218770():
    result = "undone(can't be done with script)"
    
    return result


# 218771
# Medium: The IIS 10.0 website must have a unique application pool.
def fix218771():
    result = "undone"
    try:
        command = r'%windir%\system32\inetsrv\appcmd.exe set config /section:requestFiltering /requestLimits.maxUrl:4096'
        res = subprocess.run(command , shell=True , text=True , capture_output=True)

        if "Applied" in res.stdout.strip():
            result = "done"
        else:
            result = "undone"
    except:
        result = "undone"
    
    return result


# 218772
# Medium: The maximum number of requests an application pool can process for each IIS 10.0 website must be explicitly set.
def fix218772():
    result = "undone"
    try:
        command = r'%windir%\system32\inetsrv\appcmd set config /section:system.web/sessionState /cookieless:UseCookies'
        res = subprocess.run(command , shell=True , text=True , capture_output=True)

        if "Applied" in res.stdout.strip():
            result = "done"
        else:
            result = "undone"
    except:
        result = "undone"
    
    return result


# 218773
# Medium: The amount of virtual memory an application pool uses for each IIS 10.0 website must be explicitly set.
def fix218773():
    result = "undone"
    try:
        command = r'%windir%\system32\inetsrv\appcmd.exe set config /section:access /sslFlags:SslRequireCert'
        res = subprocess.run(command , shell=True , text=True , capture_output=True)

        if "Applied" in res.stdout.strip():
            result = "done"
        else:
            result = "undone"
    except:
        result = "undone"
    
    return result

# 218774
# Medium: The amount of private memory an application pool uses for each IIS 10.0 website must be explicitly set.
def fix218774():
    result = "undone"
    try:
        command = r'%windir%\system32\inetsrv\appcmd set config /section:system.web/sessionState /mode:InProc'
        res = subprocess.run(command , shell=True , text=True , capture_output=True)

        if "Applied" in res.stdout.strip():
            result = "done"
        else:
            result = "undone"
    except:
        result = "undone"
    
    return result

# 218775
# Medium: The application pool for each IIS 10.0 website must have a recycle time explicitly set.
def fix218775():
    result = "undone"
    try:
        command = r'%windir%\system32\inetsrv\appcmd.exe set config /section:access /sslFlags:SslRequireCert'
        res = subprocess.run(command , shell=True , text=True , capture_output=True)

        if "Applied" in res.stdout.strip():
            result = "done"
        else:
            result = "undone"
    except:
        result = "undone"
    
    return result


# 218777
# Medium: The application pools rapid fail protection for each IIS 10.0 website must be enabled.
def fix218777():
    result = "undone"
    try:
        command = r'%windir%\system32\inetsrv\appcmd.exe set config /section:access /sslFlags:SslRequireCert'
        res = subprocess.run(command , shell=True , text=True , capture_output=True)

        if "Applied" in res.stdout.strip():
            result = "done"
        else:
            result = "undone"
    except:
        result = "undone"
    
    return result


# 218764
# Medium: The IIS 10.0 website must provide the capability to immediately disconnect or disable remote access to the hosted applications.
def fix218764():
    result = "undone"
    try:
        command = r'%windir%\system32\inetsrv\appcmd.exe set config /section:sites /siteDefaults.logFile.logTargetW3C:File,ETW'
        res = subprocess.run(command , shell=True , text=True , capture_output=True)
        if "Applied" in res.stdout.strip():
            result = "done"
        else:
            result = "undone"
    except:
        result = "undone"
    
    return result


# 218765
# Medium: The IIS 10.0 website must use a logging mechanism configured to allocate log record storage capacity large enough to accommodate the logging requirements of the IIS 10.0 website.
def fix218765():
    result = "undone"
    try:
        command = r'%windir%\system32\inetsrv\appcmd.exe set config /section:requestFiltering /verbs.allowUnlisted:false'
        res = subprocess.run(command , shell=True , text=True , capture_output=True)

        if "Applied" in res.stdout.strip():
            result = "done"
    except:
        result = "undone"
    
    return result

# 218766
# Medium: The IIS 10.0 websites must use ports, protocols, and services according to Ports, Protocols, and Services Management (PPSM) guidelines.
def fix218766():
    result = "undone"
    try:
        command = r'%windir%\system32\inetsrv\appcmd.exe set config /section:staticContent /remove'
        res = subprocess.run(command, shell=True, text=True, capture_output=True)
        if "Applied" in res.stdout.strip():
            result = "done"
    except:
        result = "undone"
    return result


# 218767
# Medium: The IIS 10.0 website must only accept client certificates issued by DoD PKI or DoD-approved PKI Certification Authorities (CAs).
def fix218767():
    result = "undone"
    try:
        command = r'%windir%\system32\inetsrv\appcmd.exe set config /section:staticContent /remove'
        res = subprocess.run(command, shell=True, text=True, capture_output=True)
        if "Applied" in res.stdout.strip():
            result = "done"
    except:
        result = "undone"
    return result


# 218760
# Medium: Warning and error messages displayed to clients must be modified to minimize the identity of the IIS 10.0 website, patches, loaded modules, and directory paths.
def fix218760():
    result = "undone"
    try:
        command = r'%windir%\system32\inetsrv\appcmd.exe set config /section:access /sslFlags:Ssl'
        res = subprocess.run(command, shell=True, text=True, capture_output=True)
        if "Applied" in res.stdout.strip():
            result = "done"
    except:
        result = "undone"
    return result


# 218761
# Medium: Debugging and trace information used to diagnose the IIS 10.0 website must be disabled.
def fix218761():
    result = "undone"
    try:
        command = r'%windir%\system32\inetsrv\appcmd.exe set config /section:access /sslFlags:SslNegotiateCert'
        res = subprocess.run(command, shell=True, text=True, capture_output=True)
        if "Applied" in res.stdout.strip():
            result = "done"
    except:
        result = "undone"
    return result


# 218763
# Medium: The IIS 10.0 websites connectionTimeout setting must be explicitly configured to disconnect an idle session.
def fix218763():
    result = "undone"
    try:
        command = r'%windir%\system32\inetsrv\appcmd.exe set config /section:system.webServer/httpLogging /logFile.customFields:+x-forwarded-for'
        res = subprocess.run(command, shell=True, text=True, capture_output=True)
        if "Applied" in res.stdout.strip():
            result = "done"
    except:
        result = "undone"
    return result


# 218748
# Medium: Each IIS 10.0 website must be assigned a default host header.
def fix218748():
    result = "undone"
    try:
        command = r'%windir%\system32\inetsrv\appcmd.exe set config /section:system.webServer/httpLogging /logFile.customFields:+x-forwarded-for'
        res = subprocess.run(command, shell=True, text=True, capture_output=True)
        if "Applied" in res.stdout.strip():
            result = "done"
    except:
        result = "undone"
    return result


# 218746
# Medium: The IIS 10.0 website must have Web Distributed Authoring and Versioning (WebDAV) disabled.
def fix218746():
    result = "undone"
    try:
        command = r'%windir%\system32\inetsrv\appcmd.exe set config /section:system.applicationHost/applicationPools /[name=\'DefaultAppPool\'].processModel.idleTimeout:20:00:00'
        res = subprocess.run(command, shell=True, text=True, capture_output=True)
        if "Applied" in res.stdout.strip():
            result = "done"
    except:
        result = "undone"
    return result

# 218776
# Medium: The application pools pinging monitor for each IIS 10.0 website must be enabled.
def fix218776():
    result = "undone"
    try:
        command = r'%windir%\system32\inetsrv\appcmd.exe set config /section:system.applicationHost/applicationPools /[name=\'DefaultAppPool\'].processModel.idleTimeout:20:00:00'
        res = subprocess.run(command, shell=True, text=True, capture_output=True)
        if "Applied" in res.stdout.strip():
            result = "done"
    except:
        result = "undone"
    return result


# 218759
# Directory Browsing on the IIS 10.0 website must be disabled.
def fix218759():
    result = "undone"
    try:
        command = r'%windir%\system32\inetsrv\appcmd.exe set config /section:system.applicationHost/applicationPools /[name=\'DefaultAppPool\'].processModel.idleTimeout:20:00:00'
        res = subprocess.run(command, shell=True, text=True, capture_output=True)
        if "Applied" in res.stdout.strip():
            result = "done"
    except:
        result = "undone"
    return result

init()
checks = [
        "218754" , "218755" , "218756" ,
        "218779" , "218750" , "218751" ,
        "218752" , "218753" , "218736" ,
        "218737" , "218735" , "218749" ,
        "218738" , "218739" , "218758" ,
        "218745", "218744", "218769",
        "218768", "218741", "218740",
        "218762", "218778", "218757", "218782",
        "218781", "218780", "218742", "218743",
        "218772", "218773", "218770", "218771",
        "218776", "218759", "218774", "218775",
        "218777" , "218765" , "218764" ,
        "218767" , "218766" , "218761" ,
        "218760" , "218763" , "218748" ,
        "218746"
        ]

# with open("./fix_results.csv" , "w") as file:
#     pass
# with open("./fix_results.csv" , "a") as file:
#     file.write("check_id , result\n")
#     for check in checks:
#         func = globals()[f"fix{check}"]
#         print(f"Checking {check}...")
#         val = func()
#         if(val == "done"):
#             print(Fore.GREEN + val + Style.RESET_ALL )
#         else:
#             print(Fore.RED + val + Style.RESET_ALL )
#         file.write(f"{check} , {val}\n")
#     file.close()