import socket
import threading

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.bind(('localhost',6000))
server.listen()

clients =[]

def handle_client(client_socket):
    while True:
        try:
            message = client_socket.recv(1024)
            broadcast(message,client_socket)

        except:
            clients.remove(client_socket)
            client_socket.close()
            break

def broadcast(message, sender_socket):
    print("boradcasting",message)
    for client in clients:
        print("client",client)
        if client != sender_socket:
            client.send(message)


print("Server is listening....")

while True:
    client_sock,addr = server.accept()
    print(f"Connected with {addr}")

    clients.append(client_sock)


    thread = threading.Thread(target=handle_client, args=(client_sock,))
    thread.start()

