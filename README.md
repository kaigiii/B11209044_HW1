# HW1 — 快速啟動（簡潔）

以下為啟動指引，依作業系統分為 GUI（雙擊）和終端備用指令。

macOS（雙擊執行檔）

```
./macOS_dist/HW1_server    # 啟 server（在一個視窗）
./macOS_dist/HW1_client    # 啟 client（另開一個視窗）
```

Windows（雙擊執行檔）

```
windows_dist\HW1_server.exe    # 啟 server（在一個視窗）
windows_dist\HW1_client.exe    # 啟 client（另開一個視窗）
```

- 終端備用（使用 Python）：

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
