import re

__version__ = "0.2.0"


def assign_value_to_variable(var, var_key, var_value=None, is_assign=False):
    if type(var) is not dict:
        var = dict()

    if is_assign:
        var[var_key] = var_value
    else:
        var[var_key] = dict()

    return var[var_key]


class Context:
    variables = dict()

    def set(self, var_name, var_value):
        parts = var_name.split('[', 1)
        is_complex = len(parts) > 1
        main = parts[0]

        var = assign_value_to_variable(self.variables, main)

        if is_complex:
            result = re.findall(r'\[([а-яА-Яa-zA-Z0-9_]+)]', var_name)
            result_length = len(result)
            for c, r in enumerate(result, 1):
                if result_length == c:
                    var = assign_value_to_variable(var, r, var_value, True)
                else:
                    var = assign_value_to_variable(var, r)


if __name__ == "__main__":
    context = Context()
    context.set('Услуги[0][Специалисты][0][ФИО]', "Соколова Алиса Андреевна")
    print(context.variables)
