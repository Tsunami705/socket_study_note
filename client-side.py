import socket

with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as s:
    #build connect with server
    s.connect(("127.0.0.1",1234))
    #send a message to the server(the message is a Byte Sequence,not a str,so don't forget "b")
    s.sendall(b"hello ross!")
    data=s.recv(1024)
    print("Received:",repr(data))

