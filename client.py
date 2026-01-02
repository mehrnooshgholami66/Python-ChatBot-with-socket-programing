import socket
import threading

HOST = '127.0.0.1'
PORT = 18100

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))

def receive():
    while True:
        try:
            message = client.recv(1024).decode()
            print(message)
        except:
            break

thread = threading.Thread(target=receive)
thread.start()

name = input("اسم شما: ")

while True:
    msg = input()
    message = f"{name}: {msg}"
    client.send(message.encode())
