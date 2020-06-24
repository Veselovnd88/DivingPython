import socket
from select import select

to_monitoring = []  # Пустой список, в который мы будет добавлять объекты для мониторинга
sock = socket.socket()
sock.bind(('127.0.0.1', 10001))
sock.listen()


def accept_conn(sock):
    print('Before accept')
    conn, addr = sock.accept()  # Метод ассепт выдает кортеж из двух зхачений
    print('Connection from ', addr)
    to_monitoring.append(conn)  # Добавляет клиентский сокет в список для мониторинга


def send_message(conn):
    print('Before receive')
    data = conn.recv(1024)  # сокет принимает данные
    if data:
        response = 'Hello world\n'
        conn.send(response.encode())  # Сокет шлет данные
    else:
        #  если данных нет то сокет закрывается
        print('Closing socket')
        conn.close()


def event_loop():
    while True:
        ready_to_read, _, _ = select(to_monitoring, [], [])  # read, write, errors возвращает объекты

        for soc in ready_to_read:
            if soc is sock:  # если объект - созданный нами серверный скет - вызываем его метол
                accept_conn(sock)
            else:
                send_message(soc)  # Если нет то вызываем килентский сокет


if __name__ == "__main__":
    to_monitoring.append(sock)
    event_loop()
