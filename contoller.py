import view
import logger
import model


def calc_start():
    places_1 = 2  # количество знаков округления по умолчанию при запуске программы - 2
    while True:
        view.hello(places_1)  # приветственное сообщение с количеством знаков после запятой в ответе
        try:
            info = view.get_number_info()  # получить номер пункта меню от пользователя
            view.text_line(0)  # пустая строка (0)
            if info == '1':  # меню 1 - комплексные числа
                value_a = view.get_complex_value()
                value_b = view.get_complex_value()
                action = view.get_action()  # ввод действия + - * /
            elif info == '2':  # меню 2 - рациональные числа
                value_a = view.get_float_value()
                value_b = view.get_float_value()
                action = view.get_action()
            elif info == '3':  # меню 3 - выбор знаков после запятой
                try:
                    places_1 = int(view.get_places())
                except:
                    view.text_line(2)  # сообщение об ошибке (код ошибки 2)
                    continue  # возврат в меню
                if places_1 < 0 or places_1 > 16:  # установлено максимальное ограничение в 16 знаков после запятой
                    view.text_line(3)  # сообщение об ошибке (код ошибки 3)
                continue
            elif info == '4':  # меню 4 - выход
                break
            else:
                view.text_line(1)
                continue
            view.text_line(0)
            model.init(value_a, value_b, action)  # присваиваем переменные
            result = model.do_it()  # проиводим действие
            if result == None:  # если было деление на 0
                continue
            else:
                view.view_data(result, value_a, value_b, action, places_1)  # вывод результата на экран с нужным округлением
            logger.write_log(info, value_a, value_b, action, result, places_1)  # запись в лог
            view.text_line(0)
        except:
            view.text_line(2)
