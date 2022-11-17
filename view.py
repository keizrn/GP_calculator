from decimal import Decimal


def view_data(data,value_a, value_b, action):
    print(f'{value_a}{action}{value_b} = {data}')


def get_float_value():
    '''Пользователь вводит число'''
    return Decimal(input('value = '))


def get_complex_value():
    '''Пользователь вводит комплексное число
    в формате a+bj, можно ввести только (a) тогда формат a+0j'''
    return complex(input('value = '))

def new_line():
    print()

def get_action():
    '''Пользователь вводит действие +-*/'''
    return str(input('Введите действие +-*/  = '))


def get_number_info():
    '''Выбор типа данных для работы,
    комплексные = 1, рациональные = 2
    выход из программы = 3'''
    return int(input('Введите тип данных:\n'
                     'Комплексные = 1\n'
                     'Рациональные = 2\n'
                     'Выход из программы = 3: '))


def menu_error():
    print('Ошибка выбора меню')

def input_error():
    flag = False
    while not flag:
        try:
            value = int(input('value = '))
            flag = True
        except ValueError:
                print('Введено не число')
                return value

mode = {'+': 'сумма', '-': 'разность', '*': 'произведение', '/': 'деление'}
info = {1: 'комплексные', 2: 'рациональные'}
