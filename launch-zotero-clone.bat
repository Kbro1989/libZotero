@echo off
set CHROME="C:\Program Files\Google\Chrome\Application\chrome_proxy.exe"
set APP_ID=odhbfokkiglbhidcpghglaaojkgoboci
set PROFILE_DIR=Default
set EXTENSION_URL=https://oz3ia64j4zozg.kimi.page/

%CHROME% --profile-directory=%PROFILE_DIR% --app-id=%APP_ID%

echo.
echo Launched Zotero Connector (app-id=%APP_ID%)
echo If this opens a blank window, the extension may need to be reloaded.
pause
