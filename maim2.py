import datetime
from contextlib import contextmanager


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
def logger():
    try:
        start_time = datetime.datetime.utcnow()
        yield start_time
    finally:
        finish_time = datetime.datetime.utcnow()
        work_time = finish_time - start_time
        print(f'{start_time}: {"Запуска кода"}\n{finish_time}: {"Окончания работы кода"}\n'
              f'{work_time}: {"Время работы кода"}')


with logger() as log_file:
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
