from decimal import Decimal

mode = {'+': 'сумма', '-': 'разность', '*': 'произведение', '/': 'деление'}
info = {1: 'комплексные', 2: 'рациональные'}
line_1 = {0: '', 1: 'Ошибка выбора меню', 2: 'Ошибка ввода числа'}

def view_data(data, title):
    print(f'{title} = {data}')

def get_float_value():
    return Decimal(input('value = '))

def get_complex_value():
    return complex(input('value = '))

def get_action():
    return str(input('Введите действие +-*/  = '))

def get_number_info():
    return int(input('Введите тип данных:\n'
                     'Комплексные = 1\n'
                     'Рациональные = 2\n'
                     'Выход из программы = 3: '))

def text_line(num_1):
    print(line_1[num_1])
