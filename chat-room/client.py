import socket
import threading

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(("localhost", 6000))

def receive_messages():
    while True:
        try:
            msg = client.recv(1024).decode()
            if msg:
                print("\nReceived:", msg)
                print("Enter the reply:\t")
        except:
            print("Disconnected from server")
            client.close()
            break

# Start receiver thread
threading.Thread(target=receive_messages, daemon=True).start()

# Send messages
while True:
    msg = input("Enter message: ")
    client.send(msg.encode())
