import socket
from change_text import change_text

IP="127.0.0.1"
DEFAULT_PORT=80 #default port of HTTP
BUFLEN=4500

def newClientSocket(request):
    #create a socket
    dataSocket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

    #用从服务端接收到的request读取请求的host，端口等信息
    headers=request.split(b"\r\n")
    # print(headers)
    host=headers[1].split(b':')[1].decode().strip()

    if host is None:
        print('Server not found')
        return(b'Server not found')
    else:
        pass

    print("你好+",host,DEFAULT_PORT)




    try:
        #连接服务端socket
        dataSocket.connect((host,DEFAULT_PORT)) #这里用http协议，而不是https，因此端口应为80而不是443
        print("Connect successful to website",host,"in port",DEFAULT_PORT)

        #向网站发送请求
        # new_request=f'GET {host}:{DEFAULT_PORT} HTTP/1.1\r\nHost: {host}:{DEFAULT_PORT}\r\nConnection: keep-alive\r\nAccept-Encoding: gzip, deflate\r\nAccept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7\r\n'

        #将request的method从CONNECT改为GET
        request=request.replace(b"CONNECT",b"GET")

        dataSocket.send(request)    #发送也是阻塞的
        response=b""
        while True: #若没有传送完毕，则一直接收服务器传来的数据。传送完毕之后会返回一个空的recved
            #等待接收服务端的消息
            recved=dataSocket.recv(BUFLEN)
            #如果返回空bytes，表示对方关闭了连接
            if not recved:
                break
            
            response+=recved    #考虑到TCP分多次发送报文
        print("网页的回复为：",response)
        response=change_text(response)

        dataSocket.close()
        return response
    except(socket.error):
        print(socket.error)