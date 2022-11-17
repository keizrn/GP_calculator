from decimal import Decimal

mode = {'+': 'сумма', '-': 'разность', '*': 'произведение', '/': 'деление'}
info = {1: 'комплексные', 2: 'рациональные'}
line_1 = {0: '', 1: 'Ошибка выбора меню', 2: 'Ошибка ввода числа', 3: 'Неверное количество знаков', 4: 'Деление на ноль'}

def hello(round_1):
    print(f'Это программа-калькулятор. Результат вычислений будет округлён до {round_1} знаков после запятой')

def view_data(data,value_a, value_b, action):
    print(f'{value_a} {action} {value_b} = {data}')

def get_float_value():
    return Decimal(input('value = '))

def get_complex_value():
    return complex(input('value = '))

def get_action():
    return input('Введите действие: + - * /  = ')

def get_number_info():
    return input('Выберите пункт меню:\n'
                    'Действия с комплексными числами = 1\n'
                    'Действия с рациональными числами = 2\n'
                    'Изменить количество знаков после запятой = 3\n'
                    'Выход из программы = 4: ')

def text_line(num_1):
    print(line_1[num_1])

def get_places():
    return input('Введите количество знаков после запятой в ответе. Максимум 16. ')
