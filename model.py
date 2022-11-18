import view

x = 0
y = 0
act = ''

def init(a, b, action):  # присвоение значений глобальным переменным
    global x
    global y
    global act
    x = a
    y = b
    act = action

def do_it():  # основной вычислительный блок
    if act == '+':
        return x + y
    if act == '-':
        return x - y
    if act == '*':
        return x * y
    if act == '/':
        try:
            return x / y
        except ZeroDivisionError:
            view.text_line(4)
