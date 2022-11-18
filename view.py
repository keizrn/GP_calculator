from decimal import Decimal

mode = {'+': 'сумма', '-': 'разность', '*': 'произведение', '/': 'деление'}  # словарь арифметических действий для лога
info = {1: 'комплексные', 2: 'рациональные'}  # словарь типов чисел для лога
line_1 = {0: '',
          1: 'Ошибка выбора меню\n',
          2: 'Ошибка ввода числа\n',
          3: 'Неверное количество знаков\n',
          4: 'Решения нет. Деление на ноль\n',
          5: 'Ошибка ввода действия\n'
          }  # словарь строк / сообщений об ошибках с ключами

def hello(round_1):  # приветственное сообщение с количеством знаков округления в ответе
    print(f'Это программа-калькулятор. Результат вычислений будет округлён до {round_1} знаков после запятой')

def view_data(data, value_a, value_b, action, places_0):  # вывод ответа на экран
    print(f'{value_a} {action} {value_b} =', "{0:.{1}f}".format(data, places_0))

def get_float_value():  # ввод рационального числа
    return Decimal(input('value = '))

def get_complex_value():  # ввод комплексного числа
    return complex(input('value = ').lower().replace('i', 'j'))

def get_action():  # ввод арифметического действия
    flag_sign = False
    while not flag_sign:
        temp_sign = input('Введите действие: + - * /  = ')
        flag_sign = True if temp_sign == '+' or temp_sign == '-' or temp_sign == '*' or temp_sign == '/' \
            else text_line(5)
    return temp_sign

def get_number_info():  # основное меню
    return input('Выберите пункт меню:\n'
                    'Действия с комплексными числами = 1\n'
                    'Действия с рациональными числами = 2\n'
                    'Изменить количество знаков после запятой = 3\n'
                    'Выход из программы = 4: ')

def text_line(num_1):  # вывод строки / сообщения об ошибке
    print(line_1[num_1])

def get_places():  # ввод количества знаков после запятой
    return input('Введите количество знаков после запятой в ответе. Максимум 16: ')
