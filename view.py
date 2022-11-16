from decimal import Decimal


def view_data(data,value_a, value_b, action):
    print(f'{value_a}{action}{value_b} = {data}')


def get_float_value():
    return Decimal(input('value = '))


def get_complex_value():
    return complex(input('value = '))

def new_line():
    print()

def get_action():
    return str(input('Введите действие +-*/  = '))


def get_number_info():
    return int(input('Введите тип данных:\n'
                     'Комплексные = 1\n'
                     'Рациональные = 2\n'
                     'Выход из программы = 3: '))


def menu_error():
    print('Ошибка выбора меню')


mode = {'+': 'сумма', '-': 'разность', '*': 'произведение', '/': 'деление'}
info = {1: 'комплексные', 2: 'рациональные'}
