import socket
import threading


client=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(("127.0.0.1",51372)) #ّFor example Localhost = 127.0.0.1 , Port=50505

def receive():
    while True:
        try:
            msg=client.recv(1024).decode()
            print(f"[\n new msg]:{msg}")
        except:
            print("disconnect server!")
            client.close()
            break
def send():
    while True:
        msg=input()
        try :
            client.send(msg.encode())
        except:
            print("you can't send massage")
            break

threading.Thread(target=receive).start()
threading.Thread(target=send).start()
