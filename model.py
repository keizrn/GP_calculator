
x = 0
y = 0
act = ''

def init(a, b, action):
    global x
    global y
    global act
    x = a
    y = b
    act = action

def do_it():
    if act == '+':
        return x + y
    elif act == '-':
        return x - y
    elif act == '*':
        return x * y
    elif act == '/':
        return x / y

def calculate():
 try:
        return do_it()
    except ZeroDivisionError :
        print ('Деление на 0')