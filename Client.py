import socket
import threading

host = socket.gethostname()
ip = input('')
port = 4591
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #ipv4 tcp
client_socket.connect((ip, port))
print(f"Connected to chat server at {ip}:{port}")
name = input(f"Enter your name ")
client_socket.send(name.encode('utf-8'))
def listeing_chat():
    while True:
        data = client_socket.recv(10000).decode('utf-8')
        print(f"Received from server: {data}")
def send_chat():
    while True:
        message = input("")
        client_socket.sendall((message + "\n").encode('utf-8'))

thread = threading.Thread(target=listeing_chat)
thread2 = threading.Thread(target=send_chat)
thread.start()
thread2.start()
print("Sucess")
