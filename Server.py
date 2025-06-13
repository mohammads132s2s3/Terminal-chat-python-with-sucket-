import socket
import threading

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(("127.0.0.1", 50505)) #For example Localhost=127.0.0.1 , Port=50505
s.listen()

clients = []

def handl_clint(client):
    while True:
        try:
            msg = client.recv(1024).decode()
            if not msg:
                break
            print(f"[msg]: {msg}")
            broadcast(msg, client)
        except:
            clients.remove(client)
            client.close()
            break

def broadcast(msgg, sender_socket):
    for client in clients:
        if client != sender_socket:
            try:
                client.send(msgg.encode())
            except:
                clients.remove(client)
                client.close()

while True:
    client, addr = s.accept()
    print(f"Connection from {addr}")
    clients.append(client)
    threading.Thread(target=handl_clint, args=(client,)).start()
