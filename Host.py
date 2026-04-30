import socket
import threading
host = socket.gethostname()
ip = '192.168.1.219'
port = 4591
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #ipv4 tcp 
server_socket.bind((ip, port))
server_socket.listen(5)
print(f"Chat server started on {ip}:{port}")
client_socket, addr = server_socket.accept()
Name=client_socket.recv(2048).decode('utf-8')
print(f"{Name} connected from {addr}")

def listeing_chat():
    while True:
        data = client_socket.recv(10000).decode('utf-8')
        print(f"Received from  {Name}: {data}")
def send_chat():
    while True:
        message = input("")
        client_socket.sendall((message+"\n").encode('utf-8'))

thread = threading.Thread(target=listeing_chat)
thread2 = threading.Thread(target=send_chat)
thread.start()
thread2.start()
print("Sucess")
