from datetime import datetime as dt
from view import mode, info

def write_log(type, num1, num2, func, res):
    time = dt.now().strftime('%H:%M')
    with open ('log.txt', 'a', encoding='utf-8') as file:
        file.writelines(f'Время внесения данных {time},Тип данных = {info[type]}, Число первое = {num1}, Число второе = {num2}, Действие = {mode[func]}, Результат = {res} \n')
