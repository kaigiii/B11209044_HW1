@echo off
REM Windows launcher (CMD). Place in project root and double-click to open two windows that run the server and client.
cd /d "%~dp0"
start "HW1 Server" cmd /k "windows_dist\HW1_server.exe"
start "HW1 Client" cmd /k "windows_dist\HW1_client.exe"
