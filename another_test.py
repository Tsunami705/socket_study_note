import socket

HOST = 'www.google.com'
PORT = 80
BUFFER_SIZE = 1024

def send_request():
    # Create a socket object
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Connect to the server
    client_socket.connect((HOST, PORT))

    # Send the HTTP request
    request = "GET / HTTP/1.1\r\nHost: " + HOST + "\r\nUser-Agent: Mozilla/5.0\r\n\r\n"
    client_socket.send(request.encode())

    # Receive the response
    response = client_socket.recv(BUFFER_SIZE)

    # Print the response
    print(response.decode())

    # Close the socket
    client_socket.close()

if __name__ == '__main__':
    send_request()