from socket import *
import threading

def receive_message(sock):
    while True:
        try:
            message = sock.recv(1024).decode()
            if message:
                print(message)
            else:
                sock.close()
                break
        except:
            print("An error occurred!")
            sock.close()
            break

host = "127.0.0.1"
port = 4446

s = socket(AF_INET, SOCK_STREAM)
s.connect((host, port))
print(f"Connected to chat server {host}:{port}")

threading.Thread(target=receive_message, args=(s,)).start()

while True:
    message = input('')
    if message:
        s.send(message.encode())
    else:
        s.close()
        break
