import socket



sock = socket.socket()
sock.bind(('127.0.0.1', 10001))
sock.listen()

conn, addr = sock.accept()
while True:
    print('Connection from ', addr)
    data = conn.recv(1024)
    if not data:
        break
    print(data)
conn.close()
sock.close()