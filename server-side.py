import socket
import threading

#thread function
def handle_client(c,addr):
    print(addr," connected.")

    while True:
        data=c.recv(1024)
        if not data:
            break
        c.sendall(data)


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


    # c,addr=s.accept() #accept connection of every server,and return a new socket c and server's ip address
    # with c:
    #     print(addr,"connected.")

    #     while True:
    #         data=c.recv(1024) #1024 means the socket accept maximun 1024 byte per time
    #         if not data:
    #             break
    #         c.sendall(data)


    #* important ! *
    #because of the GIL lock,python will make sure at any time , only one thread is running
    #that is ,we can not achieve the true Parallel,instead,concurrent
    