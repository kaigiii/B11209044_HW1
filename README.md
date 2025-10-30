# HW1 — 快速啟動（簡潔）

以下為最短且明確的啟動指引，依作業系統分為 GUI（雙擊）和終端備用指令。

macOS
- GUI：在專案資料夾雙擊 `run_hw1.command`（會開兩個 Terminal 視窗，分別執行 `macOS_dist/HW1_server` 與 `macOS_dist/HW1_client`）。
- 終端備用：

```bash
cd /path/to/project
./macOS_dist/HW1_server    # 啟 server（在一個視窗）
./macOS_dist/HW1_client    # 啟 client（另開一個視窗）
```

Windows
- GUI：雙擊 `run_hw1.bat`（會開兩個 cmd 視窗，執行 `windows_dist\HW1_server.exe` 與 `windows_dist\HW1_client.exe`）。
- 終端備用（有 .exe）：

```powershell
cd C:\path\to\project
windows_dist\HW1_server.exe
windows_dist\HW1_client.exe
```

- 終端備用（無 .exe，使用 Python）：

```powershell
python B11209044_hw1_server.py    # 在一個視窗
python B11209044_hw1_client.py    # 在另一個視窗
```

預期結果
- Server 會顯示：

```
The server is ready to receive
```

- Client 會顯示提示：

```
Input lowercase sentence:
```

- 在 client 輸入任意句子後按 Enter，client 會顯示 server 傳回的大寫字串。

注意（簡短）
- macOS Gatekeeper 或 Windows SmartScreen 可能對未簽名的執行檔顯示警告；若發生，請使用右鍵 → 開啟或到系統安全設定允許執行。

(完)
