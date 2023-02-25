import socket
import threading
import os

#thread function
def handle_client(c,addr):
    print(addr," connected.")

    while True:
        request=c.recv(1024)
        
        #Parse HTTP headers
        #http中定义的标准换行符是回车+换行，这就是为什么使用\r\n
        #catch http request
        print(request)
        headers=request.split(b"\r\n")
        print(headers)
        file=headers[0].split()[1].decode()
        print(file)

        WEBROOT=os.path.dirname(__file__)
        #Load file content
        if file=="/":
            file="/index.html"

        #read the content of the file
        try:
            with open(WEBROOT+file,"rb") as f:
                content=f.read()
            response=b"HTTP/1.0 200 OK\r\n\r\n"+content
        except:
            response=b"HTTP/1.0 404 NOT FOUND\r\n\r\nFile not found!"

        #Send HTTP response
        c.sendall(response)


#AF_INET means we use ipv4,SOCK_STREAM means TCP is a byteflow protocol
with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as s:
    print("hello!")
    s.bind(("0.0.0.0",1234)) #NIC and 0.0.0.0 means every NIC can use the socket to connect
    #start listen
    s.listen()

    #use multi-thread to allow multi clients connect to the server at the same time.
    while True:
        c,addr=s.accept()

        t=threading.Thread(target=handle_client,args=(c,addr))
        t.start()
