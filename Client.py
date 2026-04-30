import socket
import threading

host = socket.gethostname()
ip = ''
port = 4591
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #ipv4 tcp
client_socket.connect((ip, port))
print(f"Connected to chat server at {ip}:{port}")
def listeing_chat():
while True:
data = client_socket.recv(2048).decode('utf-8')
print(f"Received from server: {data}")
def send_chat():
while True:
message = input("")
client_socket.send(message.encode('utf-8'))

thread = threading.Thread(target=listeing_chat)
thread2 = threading.Thread(target=send_chat)
thread.start()
thread2.start()
print("Sucess")
