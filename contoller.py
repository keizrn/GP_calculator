import view
import logger
import model


def calc_start():
    places_1 = 2
    while True:
        view.hello(places_1)
        try:
            info = view.get_number_info()
            view.text_line(0)
            if info == '1':
                value_a = view.get_complex_value()
                value_b = view.get_complex_value()
                action = view.get_action()
            elif info == '2':
                value_a = view.get_float_value()
                value_b = view.get_float_value()
                action = view.get_action()
            elif info == '3':
                try:
                    places_1 = int(view.get_places())
                except:
                    view.text_line(2)
                    continue
                if places_1 < 0 or places_1 > 16:
                    view.text_line(3)
                continue
            elif info == '4':
                break
            else:
                view.text_line(1)
                continue
            view.text_line(0)
            model.init(value_a, value_b, action)
            result = model.do_it()
            if result == None:
                continue
            else:
                view.view_data(result, value_a, value_b, action, places_1)
            logger.write_log(info, value_a, value_b, action, result, places_1)
            view.text_line(0)
        except:
            view.text_line(2)
