import socket
import threading

HOST = '127.0.0.1'
PORT = 18100

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen()

clients = []

def broadcast(message, sender):
    for client in clients:
        if client != sender:
            client.send(message)

def handle_client(client):
    while True:
        try:
            message = client.recv(1024)
            broadcast(message, client)
        except:
            clients.remove(client)
            client.close()
            break

print("Server started...")

while True:
    client, addr = server.accept()
    print(f"Connected: {addr}")
    clients.append(client)

    thread = threading.Thread(target=handle_client, args=(client,))
    thread.start()
