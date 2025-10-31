# B11209044_hw1_client.py
# Client 程式
# 根據 "Computer Networking: A Top-Down Approach" 範例修改

# 從 socket 模組匯入所有功能
from socket import *

# 設定 Server 的主機名稱或 IP 位址
# 'localhost' (或 '127.0.0.1') 表示 Server 在同一台機器上執行
serverName = 'localhost'

# 設定 Server 的埠號 (必須與 Server 程式中設定的
serverPort = 12000
# 若 server 寫入了 server_port.txt，優先使用該 port（方便 server 自動選 port 的情況）
try:
	with open('server_port.txt', 'r') as f:
		data = f.read().strip()
		if data:
			serverPort = int(data)
except FileNotFoundError:
	pass
except Exception:
	# 若讀取或解析失敗，保留預設 port
	pass

# 建立 Client 的 TCP Socket
clientSocket = socket(AF_INET, SOCK_STREAM)

# 嘗試連接(connect)到指定的 Server
clientSocket.connect((serverName, serverPort))

# 提示使用者從鍵盤輸入一個句子
# 注意: input() 會讀取一行字元
sentence = input('Input lowercase sentence: ')

# 將使用者輸入的字串編碼(encode)為 bytes
# 並透過 Client Socket 傳送(send)到 Server
clientSocket.send(sentence.encode())

# 接收(recv) Server 傳回的資料 (最多 1024 bytes)
# .decode() 將收到的 bytes 轉換回 Python 字串
modifiedSentence = clientSocket.recv(1024).decode()

# 在螢幕上列印出 Server 的回應
print('From Server:', modifiedSentence)

# 關閉 Client Socket，結束連線
clientSocket.close()

# 等待使用者按任意鍵再結束（避免雙擊或啟動器視窗立刻關閉）
# 在 Windows 或其他平台上執行時，這行會顯示提示並等待輸入
try:
	input('\n按任意鍵結束...')
except Exception:
	# 若執行環境不支援標準輸入（例如某些 GUI 直譯器），則靜默結束
	pass
