$scriptDir = Split-Path -Parent $MyInvocation.MyCommand.Definition
Start-Process -FilePath "powershell" -ArgumentList "-NoExit","-Command","& '$scriptDir\dist\HW1_server.exe'"
Start-Process -FilePath "powershell" -ArgumentList "-NoExit","-Command","& '$scriptDir\dist\HW1_client.exe'"
