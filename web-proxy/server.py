import socket
import threading
from client import * 

IP="127.0.0.1"
PORT=8080
BUFLEN=4500

#线程函数
def handle_client(c,addr):
    print(addr,"connected.")

    #尝试读取对方客户端发送的请求
    #BUFLEN指定从接收缓冲里最多读取多少字节（缓冲区
    recved=c.recv(BUFLEN)

    #如果返回空bytes，表示对方关闭了连接
    #退出循环，结束消息收发


    #读取的字节数据的byte类型,需要解码为字符串
    info=recved.decode()
    print(f'收到对方信息：{info}')

    # 将从浏览器接收到的HTTP请求发送给客户端(以byte类型)
    #通过函数传递
    response=newClientSocket(recved)
    c.sendall(response)
    c.close()


#create a socket（用于监听的socket）
listenSocket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

# bind to an addr and ip
listenSocket.bind((IP,PORT))

#let socket to be listen status
#param 5 means 最多接收多少个等待连接的客户端
listenSocket.listen()
print(f'服务端启动成功，在{PORT}端口等待客户端连接。')

while True:
    #代码会被阻塞直到监听到新的客户端的连接请求并建立连接
    dataSocket,addr=listenSocket.accept()   #创建一个新的，用于传输数据的socket，与这个客户端绑定
    print('接收一个客户端连接：',addr)
    #创建多个线程
    t=threading.Thread(target=handle_client,args=(dataSocket,addr))
    t.start()

listenSocket.close()


