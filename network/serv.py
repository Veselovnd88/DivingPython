import socket



sock = socket.socket()
sock.bind(('127.0.0.1', 10001))
sock.listen()


while True:
    print('Before accept')
    conn, addr = sock.accept()
    print('Connection from ', addr)
    while True:
        print('Before receive')
        data = conn.recv(1024)
        if not data:
            break
        else:
            response = 'Hello world\n'
            conn.send(response.encode())
    print('Outside inner loop')
    conn.close()
