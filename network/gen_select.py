import socket
from select import select

to_read = {}  # словарь с сокетами на чтение
to_write = {}  # словарь с сокетами на передачу (запись)
tasks = []  # список куда будут отдаваться функции


def server():
    sock = socket.socket()  # читаем
    sock.bind(('127.0.0.1', 10001))
    sock.listen()

    while True:
        print("Запуск Read Sock")
        yield ('read', sock)
        print('Before accept')
        cl_sock, addr = sock.accept()  # читаем
        print('Connection from ', addr)
        tasks.append(client(cl_sock))  # В список добавляется функRция клиентского сокета


def client(cl_sock):
    while True:
        print("Запуск read клиентский сокет ")
        yield ('read', cl_sock)  # передается параметр рид и клиентский сокет
        print('Before receive')
        data = cl_sock.recv(1024)  #  прием информации из клиентского сокета
        if not data:
            break
        else:
            response = 'Hello world\n'
            print('Запуск клиентского сокета на чтение')
            yield ('write', cl_sock)  # вызов клиентского сокета для записи
            cl_sock.send(response.encode())  # пишем
    print('Outside inner loop')
    cl_sock.close()


def event_loop():
    print("Запуск Евент Лупа")
    while any([tasks, to_read, to_write]):  # Выполнение цикла если хотя бы один элем полный
        while not tasks:  # Если задач нет ( а в начале они есть)
            print('Задач нет')
            ready_to_read, ready_to_write, _ = select(to_read, to_write, [])
            print(to_read, to_write)
            for soc in ready_to_read:
                tasks.append(to_read.pop(soc))
            for soc in ready_to_write:
                tasks.append(to_write.pop(soc))

        try:
            print('Блок трай')
            task = tasks.pop(0)
            reason, soc = next(task)  #сначала сюда попадает серверный сокет(рид), далее
            #  функция с илда
            if reason == 'read':
                to_read[soc] = task  #  запись в словарь - ключ сокет: значение илд(генератор)
            if reason == 'write':
                to_write[soc] = task
        except StopIteration:
            pass


tasks.append(server())

event_loop()
