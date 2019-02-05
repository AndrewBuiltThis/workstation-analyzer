@ECHO off
REM Title : GTG Workstation Analyzer
REM Objective : This application is intended to collect information on a client's workstation to understand its current state and performance.
REM Author : Andrew Valenski, Enterprise GIS Consultant, Geographic Technologies Group (GTG)
REM Date : 1/30/2019
REM ToS : This application was built to support the Enterprise GIS Consulting division of GTG. This application cannot be sold and/or included in the build of a product or service provided for compensation or payment. All references to GTG or Andrew Valenski must remain in this application. If this application is used by you, your organization or for your organization's benefit, GTG must be given credit/acknowledgement.
REM License : MIT
REM Additional Info : Geographic Technologies Group (GTG) is one of the country's leading full-service local government GIS consulting companies. GTG has been helping town, city and county governments realize the full potential of GIS for over 20 years. More information can be found on GTG's website : https://geotg.com/

SETLOCAL ENABLEDELAYEDEXPANSION
:START
ECHO.
ECHO Welcome to the to Workstation Analyzer
ECHO       built by Andrew Valenski of 
ECHO      ___                         ___     
ECHO     /\__\                       /\__\    
ECHO    /:/ _/_         ___         /:/ _/_   
ECHO   /:/ /\  \       /\__\       /:/ /\  \  
ECHO  /:/ /::\  \     /:/  /      /:/ /::\  \ 
ECHO /:/__\/\:\__\   /:/__/      /:/__\/\:\__\
ECHO \:\  \ /:/  /  /::\  \      \:\  \ /:/  /
ECHO  \:\  /:/  /  /:/\:\  \      \:\  /:/  / 
ECHO   \:\/:/  /   \/__\:\  \      \:\/:/  /  
ECHO    \::/  /         \:\__\      \::/  /   
ECHO     \/__/           \/__/       \/__/    
ECHO.
ECHO ***** Geographic Technologies Group *****
ECHO   *************************************
ECHO.
ECHO This is a Pythonic (2.7) application to collect
ECHO information on your workstation, including:
ECHO     * Identification Info (IP, Host, Domain)
ECHO     * Specfications (OS, OS Version, Processor, 32/64)
ECHO     * Performance (RAM, CPU, Storage)
ECHO     * Network Details (NICs, Errors)
ECHO     * Network Speed (Internal and External)
ECHO     * Windows Services
ECHO     * Open Ports
ECHO.
ECHO.
PAUSE
TIMEOUT 1 > NUL
CLS

ECHO.
ECHO  ##### 
ECHO #     # 
ECHO #       
ECHO #  #### 
ECHO #     # 
ECHO #     # 
ECHO  #####   
ECHO.
ECHO.
ECHO            Let's Get Started!
ECHO               ************   
ECHO.
ECHO There are three sections you will complete:
ECHO               * Your Info
ECHO         * The Organization's Info
ECHO        * Local Network information
ECHO.
PAUSE
TIMEOUT 1 > NUL
CLS

ECHO.
ECHO  ##### 
ECHO #     # 
ECHO #       
ECHO #  #### 
ECHO #     # 
ECHO #     # 
ECHO  #####   
ECHO.
ECHO.
ECHO         Pre-Analysis Confirmation:
ECHO               ************   
ECHO.
ECHO Confirm : This is a Windows Machine, You Have Python 2.7+ Installed on This Machine, You Have the Appropriate Python Libraries Installed (instructions can be found here: https://github.com/AndrewBuiltThis/gtg-workstation-analyzer) and You Have the Expressed Permission from Both the Machine's Owner and the Machine's Organization to Run This Analysis :  
ECHO.
ECHO A. "Yes"
ECHO B. "No"
ECHO.
CHOICE /C AB /N /T 15 /D A /M "Confirm to Continue [A,B] : "
IF ERRORLEVEL 1 SET USERCONFIRM="TRUE"
IF ERRORLEVEL 2 SET USERCONFIRM="FALSE"
ECHO.
TIMEOUT 1 > NUL
IF [%USERCONFIRM%] EQU ["TRUE"] GOTO COLLECT_USER_INFO
IF [%USERCONFIRM%] EQU ["FALSE"] GOTO EXIT_SETUP

:COLLECT_USER_INFO
SETLOCAL ENABLEDELAYEDEXPANSION 
ECHO.
ECHO  ##### 
ECHO #     # 
ECHO #       
ECHO #  #### 
ECHO #     # 
ECHO #     # 
ECHO  #####   
ECHO.
ECHO.
ECHO        SECTION I: Who Are You?
ECHO           ***************
ECHO.
ECHO Question 1: What's Your Name?
ECHO.
SET /p TESTINGUSER=Provide Your Name : 
IF ["%TESTINGUSER%"] EQU [] GOTO COLLECT_USER_INFO 
IF ["%TESTINGUSER%"] NEQ [] ECHO Hello, "%TESTINGUSER%". Continuing ...

TIMEOUT 2 > NUL
ECHO.
ECHO ---------------------------------------------------
ECHO.
ECHO Question 2: Why Are You Running This Workstation Analysis?
ECHO.
ECHO A. "Enjoyment / Leisure"
ECHO B. "Gathering Organization Metrics"
ECHO C. "Learning / Education"
ECHO D. "Testing Client Machine Performance"
ECHO E. "Troubleshooting"
ECHO F. "Other"
ECHO.
CHOICE /C ABCDEF /N /T 15 /D F /M "Select Reason [A,B,C,D,E,F] : "
IF ERRORLEVEL 1 SET TESTINGREASON="Enjoyment / Leisure"
IF ERRORLEVEL 2 SET TESTINGREASON="Gathering Organization Metrics"
IF ERRORLEVEL 3 SET TESTINGREASON="Learning / Education"
IF ERRORLEVEL 4 SET TESTINGREASON="Testing Client Machine Performance"
IF ERRORLEVEL 5 SET TESTINGREASON="Troubleshooting"
IF ERRORLEVEL 6 SET TESTINGREASON="Other"
ECHO.
ECHO Analysis Performed for %TESTINGREASON% Purposes. Continuing ... 
TIMEOUT 2 > NUL
CLS
GOTO COLLECT_ORG_INFO

:COLLECT_ORG_INFO
ECHO.
ECHO  ##### 
ECHO #     # 
ECHO #       
ECHO #  #### 
ECHO #     # 
ECHO #     # 
ECHO  #####   
ECHO.
ECHO.
ECHO        SECTION II: Tell Me About the Org
ECHO           **************************
ECHO.
ECHO Question 1: What's the Client Organization's Name?
ECHO [hint : this is the organization who owns the workstation]
ECHO.
ECHO.
SET /p CLIENTORG=Client Organization's Name : 
IF ["%CLIENTORG%"] EQU [] GOTO COLLECT_ORG_INFO 
IF ["%CLIENTORG%"] NEQ [] ECHO  "%CLIENTORG%" Machine Being Evaluated. Continuing ...
TIMEOUT 2 > NUL
ECHO.
ECHO ---------------------------------------------------
ECHO.
ECHO Question 2: What Type of Organization Is This?
ECHO.
ECHO A. "Community Organization"
ECHO B. "Educational Institution"
ECHO C. "Governmental Organization"
ECHO D. "Private Business"
ECHO E. "Other"
ECHO.
CHOICE /C ABCDE /N /T 15 /D E /M "Select Type [A,B,C,D,E] : "
IF ERRORLEVEL 1 SET CLIENTTYPE="Community Organization"
IF ERRORLEVEL 2 SET CLIENTTYPE="Educational Institution"
IF ERRORLEVEL 3 SET CLIENTTYPE="Governmental Organization"
IF ERRORLEVEL 4 SET CLIENTTYPE="Private Business"
IF ERRORLEVEL 5 SET CLIENTTYPE="UNKNOWN"
ECHO.
ECHO Organization Type : %CLIENTTYPE% . Continuing ... 
TIMEOUT 2 > NUL
ECHO.
ECHO ---------------------------------------------------
ECHO.
ECHO Question 3 : About How Many Employees Does This Organization Have?
ECHO.
ECHO A. "0 - 10"
ECHO B. "10 - 50"
ECHO C. "50 - 200"
ECHO D. "200 - 500"
ECHO E. "500 - 1000"
ECHO F. "1000+"
ECHO G. "I Can't Estimate"
ECHO.
CHOICE /C ABCDEFG /N /T 15 /D G /M "Select Size [A,B,C,D,E,F,G] : "
IF ERRORLEVEL 1 SET CLIENTSIZE="0 - 10"
IF ERRORLEVEL 2 SET CLIENTSIZE="10 - 50"
IF ERRORLEVEL 3 SET CLIENTSIZE="50 - 200"
IF ERRORLEVEL 4 SET CLIENTSIZE="200 - 500"
IF ERRORLEVEL 5 SET CLIENTSIZE="500 - 1000"
IF ERRORLEVEL 6 SET CLIENTSIZE="1000+"
IF ERRORLEVEL 7 SET CLIENTSIZE="UNKNOWN"
ECHO.
ECHO Organization Size : %CLIENTSIZE% . Continuing ... 
TIMEOUT 2 > NUL
ECHO.
ECHO ---------------------------------------------------
ECHO.
ECHO Question 4: Who is the Organization's Primary Contact?
ECHO.
SET /p CLIENTPOC=Organization's Primary Contact : 
IF ["%CLIENTPOC%"] EQU [] GOTO COLLECT_ORG_INFO
IF ["%CLIENTPOC%"] NEQ [] ECHO The Client Organization's Primary POC is "%CLIENTPOC%". Continuing ...  
ECHO.
TIMEOUT 2 > NUL
ECHO ---------------------------------------------------
ECHO.
ECHO Question 5: Who's Machine Is This?
ECHO.
SET /p CLIENTMACHINEOWNER=Machine Owner's Name : 
IF "[%CLIENTMACHINEOWNER%"] EQU [] GOTO COLLECT_ORG_INFO
IF ["%CLIENTMACHINEOWNER%"] NEQ [] ECHO This Machine Belongs to "%CLIENTMACHINEOWNER%". Continuing ...
TIMEOUT 1 > NUL
ECHO.
ECHO.
ECHO.
ECHO.
ECHO.
ECHO Organization Summary : 
ECHO Organization Name - "%CLIENTORG%"
ECHO Organization Type - %CLIENTTYPE%
ECHO Organization Size - %CLIENTSIZE%
ECHO Organization POC - "%CLIENTPOC%"
ECHO Machine POC - "%CLIENTMACHINEOWNER%"
TIMEOUT 3 > NUL
CLS
GOTO COLLECT_NETWORK_INFO


:COLLECT_NETWORK_INFO
ECHO.
ECHO  ##### 
ECHO #     # 
ECHO #       
ECHO #  #### 
ECHO #     # 
ECHO #     # 
ECHO  #####   
ECHO.
ECHO.
ECHO       SECTION III: Tell Me About The Network?
ECHO          *******************************
ECHO.
ECHO Question 1: What IP Do You Want To Test Against?
SET /p TESTIP=Provide IP Address [Press Enter to Test Locally] : 
IF ["%TESTIP%"] NEQ [""] ECHO "%TESTIP%" Will Be Tested. Continuing ...
IF ["%TESTIP%"] EQU  [""] (
    SET TESTIP="127.0.0.1"
    ECHO No IP Provided. Using 127.0.0.1 as Fallback. Continuing ... 
)
TIMEOUT 2 > NUL
ECHO.
ECHO ---------------------------------------------------
ECHO.
ECHO Question 2: Which Port Do You Want to Use for Network Testing? 
ECHO.
ECHO A. "80"
ECHO B. "443"
ECHO C. "Default"
ECHO.
CHOICE /C ABC /N /T 15 /D C /M "Select Port [A,B,C] : "
IF ERRORLEVEL 1 SET NETWORKPORT="80"
IF ERRORLEVEL 2 SET NETWORKPORT="443"
IF ERRORLEVEL 3 SET NETWORKPORT="80"
ECHO.
ECHO Port %NETWORKPORT% Selected. Continuing ... 
TIMEOUT 2 > NUL
ECHO.
ECHO ---------------------------------------------------
ECHO.
ECHO [Optional] Question 3: What External Website Should Be Used for Testing?
SET /p EXTERNALURL=Provide the URL [Press Enter to Skip] : 
IF [%EXTERNALURL%] EQU  [] (
    SET EXTERNALURL="github.com"
    ECHO No URL. Using github.com as Fallback. Continuing ... 
)
IF [%EXTERNALURL%] NEQ [] ECHO "%EXTERNALURL%" Will Be Tested. Continuing ...
TIMEOUT 1 > NUL
ECHO.
ECHO ---------------------------------------------------
ECHO.
ECHO [Optional] Question 4: What LAN Address Should Be Used for Testing?
SET /p LANURL=Provide LAN URL [Press Enter to Skip] : 
IF [%LANURL%] EQU [] (
    SET LANURL="EMPTYURLPARAMETER"
    ECHO No LAN URL Will Be Tested. Continuing ... 
)
TIMEOUT 1 > NUL
ECHO.
ECHO ---------------------------------------------------
ECHO.
ECHO [Optional] Question 5: What WAN Address Should Be Used for Testing?
SET /p WANURL=Provide WAN URL [Press Enter to Skip] : 
IF [%WANURL%] EQU [] (
    SET WANURL="EMPTYURLPARAMETER"
    ECHO No WAN URL Will Be Tested. Continuing ...
)
TIMEOUT 1 > NUL
ECHO.
ECHO.
ECHO.
ECHO.
ECHO.
ECHO.
ECHO Network Summary : 
ECHO Pingtest IP - "%TESTIP%"
ECHO Pingtest Port - %NETWORKPORT%
ECHO External Test URL - "%EXTERNALURL%"
ECHO LAN Test URL - "%LANURL%"
ECHO WAN Test URL - "%WANURL%"
TIMEOUT 3 > NUL
ECHO.
CLS
GOTO RUN_ANALYSIS

:RUN_ANALYSIS
ECHO.
ECHO  ##### 
ECHO #     # 
ECHO #       
ECHO #  #### 
ECHO #     # 
ECHO #     # 
ECHO  #####   
ECHO.
ECHO.
ECHO             Running Analysis
ECHO                ***********
ECHO.
python analysis.py "%TESTINGUSER%" %TESTINGREASON% "%CLIENTORG%" %CLIENTTYPE% %CLIENTSIZE% "%CLIENTPOC%" "%CLIENTMACHINEOWNER%" "%TESTIP%" %NETWORKPORT% "%EXTERNALURL%" "%LANURL%" "%WANURL%"
ECHO.
PAUSE
CLS
GOTO EXIT

:EXIT_SETUP
ECHO.
ECHO  ##### 
ECHO #     # 
ECHO #       
ECHO #  #### 
ECHO #     # 
ECHO #     # 
ECHO  #####   
ECHO.
ECHO.
ECHO                     Workstation Analysis Setup
ECHO                        ********************
ECHO.
ECHO           Instructions for deployment can be found here : 
ECHO      https://github.com/AndrewBuiltThis/gtg-workstation-analysis
ECHO.
ECHO.
ECHO                    Opening Documentation Momentarily ...
TIMEOUT 3 > NUL
START "" https://github.com/AndrewBuiltThis/gtg-workstation-analysis
START "" https://www.youtube.com/watch?v=gD4eulxGNok
START "" https://docs.python.org/2/installing/index.html
START "" https://geotg.com
ECHO.
ECHO.
ECHO.
ECHO                 Please Follow the Relevant Instructions
ECHO         After You've Set Up Your Environment, Then Relaunch This App
ECHO.
ECHO.
TIMEOUT 15
CLS

:EXIT
ECHO.
ECHO  ##### 
ECHO #     # 
ECHO #       
ECHO #  #### 
ECHO #     # 
ECHO #     # 
ECHO  #####   
ECHO.
ECHO.
ECHO                        All Done!
ECHO                          *****
ECHO.
ECHO Review the JSON file in this directory called results.json
START "" "output/index.html" 
ECHO.
ECHO      ___                         ___     
ECHO     /\__\                       /\__\    
ECHO    /:/ _/_         ___         /:/ _/_   
ECHO   /:/ /\  \       /\__\       /:/ /\  \  
ECHO  /:/ /::\  \     /:/  /      /:/ /::\  \ 
ECHO /:/__\/\:\__\   /:/__/      /:/__\/\:\__\
ECHO \:\  \ /:/  /  /::\  \      \:\  \ /:/  /
ECHO  \:\  /:/  /  /:/\:\  \      \:\  /:/  / 
ECHO   \:\/:/  /   \/__\:\  \      \:\/:/  /  
ECHO    \::/  /         \:\__\      \::/  /   
ECHO     \/__/           \/__/       \/__/    
ECHO.
ECHO ***** Geographic Technologies Group *****
ECHO   *************************************
ECHO.
ECHO.
ECHO Check out https://geotg.com/ to get in touch!
TIMEOUT 15