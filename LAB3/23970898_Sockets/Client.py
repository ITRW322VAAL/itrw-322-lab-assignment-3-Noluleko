import socket

Host = '127.0.01'
Port = 9999

with socket.socket(socket.Af_INET, socket.SOCK_STREAM) as s:
s.connect((Host, Port))
s.sendall(b'Hello, Server')
data = s.recv(1024)

print('Recieved', repr(data))