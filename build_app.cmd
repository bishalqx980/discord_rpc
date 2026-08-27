@echo off
color a
setlocal
set "INFO=[+]"

echo ================================
echo         DiscordRPC Builder
echo ================================
echo.

color 2

echo %INFO% installing dependencies...

start "" /wait cmd /c "pip install -r requirements.txt"
start "" /wait cmd /c "pip install pyinstaller"

echo %INFO% dependencies installed successfully.

echo.
echo %INFO% Building executable...

pyinstaller ^
--clean ^
--onefile ^
--uac-admin ^
--icon=icon.ico ^
--name DiscordRPC ^
app\__main__.py

echo.
echo %INFO% Build complete!
pause
