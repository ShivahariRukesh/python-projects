import socket
from utils import create_index_html_file
# Establishing a server and listening to the requests 

# creates socket object
# socket.AF_INET : Use IPv4 addresses (like 127.0.0.1, 192.168.x.x)
# socket.SOCK_STREAM : Use TCP (reliable, connection-based communication)

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('0.0.0.0',8000))

# Maximum 1 waiting connection in the queue
server.listen(1)

# print("Web server is running on port 8000,,,")

                    


create_index_html_file()
# Respond back to the triggered request
while True:

    # Blocks execution (waits)
    # Until a client connects
    # When someone connects:
    # client_socket → new socket for that client
    # addr → client’s address 

    client_socket, addr = server.accept()
    print("The connected client is\t", addr)

    #recv(1024) → Read up to 1024 bytes of data from the client
    # .decode('utf-8') → Convert bytes → readable string
    request = client_socket.recv(1024).decode('utf-8')

    headers = request.split('\n')
    filename = headers[0].split()[1]

    if filename == '/':
        filename = '/index.html'

    try:
        fin = open(filename[1:],'r')
        content = fin.read()
        fin.close()

# double "\n" → blank line separates headers from body so there should be double new line spaces
        response = "HTTP/1.1 200 OK\n\n" + content

    except FileNotFoundError:
        response = "HTTP/1.1 404 NOT FOUND\n\nFILE NOT FOUND!"

    client_socket.sendall(response.encode('utf-8'))
    client_socket.close()

