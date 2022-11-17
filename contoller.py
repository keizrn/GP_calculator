import view
import logger
import model

def calc_start():
    while True:
        try:
            info = view.get_number_info()
            view.text_line(0)
            if info == 1:
                value_a = view.get_complex_value()
                value_b = view.get_complex_value()
                action = view.get_action()
            elif info == 2:
                value_a = view.get_float_value()
                value_b = view.get_float_value()
                action = view.get_action()
            elif info == 3:
                break
            else:
                view.text_line(1)
                view.text_line(0)
                continue
            view.text_line(0)
            model.init(value_a, value_b, action)
            result = model.do_it()
            view.view_data(result, value_a, value_b, action)
            logger.write_log(info, value_a, value_b, action, result)
            view.text_line(0)
        except:
            view.text_line(2)
            view.text_line(0)


