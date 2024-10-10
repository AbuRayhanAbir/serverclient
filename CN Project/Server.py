from socket import *
import threading

host = "127.0.0.1"
port = 4446
clients = []

def client_thread(connection, address):
    while True:
        try:
            message = connection.recv(1024).decode()
            if message:
                print(f"Message from {address}: {message}")
                broadcast(message, connection)
            else:
                remove(connection)
                break
        except:
            continue

def broadcast(message, connection):
    for client in clients:
        if client != connection:
            try:
                client.send(message.encode())
            except:
                remove(client)

def remove(connection):
    if connection in clients:
        clients.remove(connection)

s = socket(AF_INET, SOCK_STREAM)
s.bind((host, port))
s.listen(5)
print(f"Server is listening on {host}:{port}")

while True:
    q, addr = s.accept()
    clients.append(q)
    print(f"Connected with {addr[0]}:{addr[1]}")
    threading.Thread(target=client_thread, args=(q, addr)).start()
