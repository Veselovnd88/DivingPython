def gen(n):
    for i in range(n):
        yield i


def gen1(name):
    for i in name:
        yield i


tasks = [gen(4), gen1('dog')]

while tasks:
    task = tasks.pop(0)
    try:
        i = next(task)
        print(i)
        tasks.append(task)
    except StopIteration:
        pass
