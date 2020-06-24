import socket
from select import select

to_read = {}
to_write = {}
tasks = []


def server():
    sock = socket.socket()  # читаем
    sock.bind(('127.0.0.1', 10001))
    sock.listen()

    while True:
        yield ('read', sock)
        print('Before accept')
        cl_sock, addr = sock.accept()  # читаем
        print('Connection from ', addr)
        tasks.append(client(cl_sock))


def client(cl_sock):
    while True:
        yield ('read', cl_sock)
        print('Before receive')
        data = cl_sock.recv(1024)
        if not data:
            break
        else:
            response = 'Hello world\n'
            yield ('write', cl_sock)
            cl_sock.send(response.encode())  # пишем
    print('Outside inner loop')
    cl_sock.close()


def event_loop():
    while any([tasks, to_read, to_write]):
        while not tasks:
            ready_to_read, ready_to_write, _ = select(to_read, to_write, [])
            for soc in ready_to_read:
                tasks.append(to_read.pop(soc))
            for soc in ready_to_write:
                tasks.append(to_write.pop(soc))

        try:
            task = tasks.pop(0)
            reason , soc = next(task)
            if reason == 'read':
                to_read[soc] = task
            if reason == 'write':
                to_write[soc] = task
        except StopIteration:
            pass
tasks.append(server())

event_loop()
