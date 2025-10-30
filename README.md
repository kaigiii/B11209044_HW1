# HW1 — 啟動說明（最簡短）

以下列出每個作業系統的快速啟動（GUI）方法、備用的終端機指令，以及預期成果。

macOS
- GUI（推薦）：雙擊 `run_hw1.command`（會開兩個 Terminal 視窗，分別執行 `macOS_dist/HW1_server` 與 `macOS_dist/HW1_client`）。
- 備用（終端機）：

```bash
./macOS_dist/HW1_server    # 啟 server
./macOS_dist/HW1_client    # 啟 client
```

Windows
- GUI（若已建置 `.exe`）：雙擊 `run_hw1.bat`（會開兩個 cmd 視窗，執行 `windows_dist\\HW1_server.exe` 與 `windows_dist\\HW1_client.exe`）。
- 備用（命令提示字元 / PowerShell）：

如果有 `.exe`：
```powershell
windows_dist\\HW1_server.exe
windows_dist\\HW1_client.exe
```

如果使用 Python（未建置 `.exe`）：
```powershell
python B11209044_hw1_server.py
# 在另一個視窗
python B11209044_hw1_client.py
```

Linux
- 備用（終端機）：

```bash
python3 B11209044_hw1_server.py &
python3 B11209044_hw1_client.py
```

預期成果（所有平台相同）
- Server 會印出：

```
The server is ready to receive
```

- Client 會提示：

```
Input lowercase sentence:
```

- 在 client 輸入任意句子並按 Enter，client 應顯示 server 回傳的全大寫字串。

備註
- 若要產生 Windows `.exe`，請在 Windows 平台上使用 PyInstaller（或在 CI 的 Windows runner 上建置）。

(完)
