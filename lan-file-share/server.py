import socket
import os

SERVER_IP = '0.0.0.0'
PORT = 8080
BUFFER_SIZE = 3024
SEPARATOR = "<SEPARATOR>"


server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((SERVER_IP, PORT))
server.listen()

print(f"Listening on {SERVER_IP}:{PORT}")

client_socket, client_address = server.accept()
print("Connection from {}".format(client_address))

received = client_socket.recv(BUFFER_SIZE).decode()
filename, filesize = received.split(SEPARATOR)

filename = os.path.basename(filename)
filesize = int(filesize)

print(f"Receiving file: {filename} of File size: {filesize} bytes")

client_socket.send(b"OK")

bytes_received =0

with open(filename, "wb") as f:
    while bytes_received < filesize:
        bytes_read = client_socket.recv(BUFFER_SIZE)
        if not bytes_read:
            break

        f.write(bytes_read)
        bytes_received += len(bytes_read)

print("File Transfer is completed from client to server")

client_socket.close()
server.close()