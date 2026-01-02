import socket

# Establishing a server and listening to the requests 

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('0.0.0.0',8000))
server.listen(1)

print("Web server is running on port 8000,,,")

# Respond back to the triggered request
while True:
    client_socket, addr = server.accept()
    request = client_socket.recv(1024).decode('utf-8')

    headers = request.split('\n')
    filename = headers[0].split()[1]

    if filename == '/':
        filename = '/index.html'

    try:
        fin = open(filename[1:],'r')
        content = fin.read()
        fin.close()


        response = "HTTP/1.1 200 OK\n" + content

    except FileNotFoundError:
        response = "HTTP/1.1 404 NOT FOUND\nFILE NOT FOUND!"

    client_socket.sendall(response.encode('utf-8'))
    client_socket.close()