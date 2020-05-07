import datetime
from contextlib import contextmanager


def write_log_time(log_file, action):
    log_file.write(f'{datetime.datetime.utcnow()}: {action}\n')
    return datetime.datetime.utcnow()


def write_log_work_time(log_file, start_time, finish_time, action):
    log_file.write(f'{finish_time - start_time}: {action}\n')


def addition(data):
    print(int(data[1]) + int(data[2]))


def subtraction(data):
    print(int(data[1]) - int(data[2]))


def multiplication(data):
    print(int(data[1]) * int(data[2]))


def division(data):
    print(int(data[1]) / int(data[2]))


def operation_definition(data):
    if data[0] == '+':
        addition(data)
    elif data[0] == '-':
        subtraction(data)
    elif data[0] == '*':
        multiplication(data)
    elif data[0] == '/':
        division(data)


@contextmanager
def logger(path, encoding='utf-8'):
    try:
        file = open(path, 'a', encoding=encoding)
        start_time = write_log_time(file, 'start')
        yield file, start_time
    finally:
        finish_time = write_log_time(file, 'end')
        write_log_work_time(file, start_time, finish_time, 'work time')
        file.close()


with logger('mylog.log') as log_file:
    command = input('Введите данные: ').split()

    assert len(command[0]) == 1, "Вводите значения через пробел ' '"
    assert command[0] in ('+', '-', '*', '/'), "Вы ввели неверные данные"
    assert (len(command) == 3), "Вы ввели невернное кол-во символов"

    try:
        operation_definition(command)
    except ZeroDivisionError as e:
        print(e)
    except ValueError as e:
        print(e)
    except IndexError as e:
        print(e)
