import socket
from change_text import change_text

HOST='www.google.com'
PORT=80
BUFFER_SIZE=1024

client_socket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

#连接到网站
client_socket.connect((HOST,PORT))

#向网站发送GET请求
request='GET / HTTP/1.1\r\nHost: {HOST}\r\nUser-Agent: Mozilla/5.0\r\nConnection: keep-alive\r\nAccept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7 \r\nAccept-Encoding: gzip, deflate\r\nAccept-Language: zh-CN,zh;q=0.9,en;q=0.8,no;q=0.7\r\n\r\n'
client_socket.send(request.encode())
whole_res=b''
f=open("data.txt","w",encoding='utf-8')


recved=client_socket.recv(1024)
whole_res=recved
# while True:
#     recved=client_socket.recv(1024)
#     if not recved:
#         break
#     whole_res+=recved

print("连接成功")
whole_res=change_text(whole_res)
f.write(whole_res.decode())
client_socket.close()