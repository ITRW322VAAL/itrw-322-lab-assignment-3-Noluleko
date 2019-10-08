import socket

Host = "127.0.8.1"
Port = 9999
with socket.socket(.AF_Inet, socket.SOCK_STREAM) as s:
s.bind((HOST,PORT))
s.listen()
conn,addr  = s.accept()
with conn:
print('Server is connected with address',addr)
while True:
data = conn.recv(2048)
if not data:
break
conn.sendall(data)