import socket
import os

SERVER_IP = '0.0.0.0'
PORT = 8080
BUFFER_SIZE = 3024
SEPARATOR = "<SEPARATOR>"

filename = 'hello.txt'
filesize = os.path.getsize(filename)

client= socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((SERVER_IP, PORT))

print("Connected to the server")

client.send("{}{}{}".format(filename,SEPARATOR,filesize).encode())

client.recv(BUFFER_SIZE)

with open(filename, "rb") as f:
    while True:
        bytes_read = f.read(BUFFER_SIZE)
        if not bytes_read:
            break
        client.sendall(bytes_read)

print("File Sent Successfully")

client.close()