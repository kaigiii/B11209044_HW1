# B11209044_hw1_server.py
# Server 程式
# 根據 "Computer Networking: A Top-Down Approach" 範例修改

# 從 socket 模組匯入所有功能
from socket import *

# 設定伺服器埠號
serverPort = 12000

# 建立伺服器的 TCP Socket
# AF_INET 表示使用 IPv4
# SOCK_STREAM 表示使用 TCP
serverSocket = socket(AF_INET, SOCK_STREAM)
# 允許重複使用本地位址（在 server 非正常關閉後可快速重啟）
serverSocket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)

# 將 Socket 綁定(bind)到指定埠號
# ' ' 空字串表示伺服器會監聽所有本機可用的 IPv4 位址
serverSocket.bind(('127.0.0.1', serverPort))

# 開始監聽(listen)連線請求
# 參數 1 表示系統在拒絕新連線前，最多允許 1 個連線在佇列中等待
serverSocket.listen(1)

print('The server is ready to receive')

# 進入無限迴圈，持續等待 Client 連線
while 1:
    # 當 Client 連線時，接受(accept)連線
    # 建立一個新的專用 Socket (connectionSocket) 來與該 Client 通訊
    # addr 儲存了 Client 的位址資訊
    connectionSocket, addr = serverSocket.accept()
    
    # 從 Client 接收資料 (最多 1024 bytes)
    # .decode() 將從網路收到的 bytes 轉換為 Python 字串
    sentence = connectionSocket.recv(1024).decode()
    
    # 將接收到的字串轉換為大寫
    capitalizedSentence = sentence.upper()

    # 將處理後的大寫字串編碼(encode)回 bytes
    # 透過 connectionSocket 傳送(send)回 Client
    connectionSocket.send(capitalizedSentence.encode())
    
    # 關閉與此 Client 的連線 Socket
    # Server Socket (serverSocket) 仍然開啟，繼續等待下一個連線
    connectionSocket.close()
