import view
import logger
import model

def clac_start():
    info = view.get_number_info()
    if info == 1 or info == 2:
        if info == 1:
            value_a = view.get_complex_value()
            print(value_a)
            value_b = view.get_complex_value()
            print(value_b)
            action = view.get_action()

        elif info == 2:
            value_a = view.get_float_value()
            value_b = view.get_float_value()
            action = view.get_action()

        model.init(value_a, value_b, action)
        result = model.do_it()
        view.view_data(result, "result")
        logger.write_log(info, value_a, value_b, action, result)
    else: print('Error')
