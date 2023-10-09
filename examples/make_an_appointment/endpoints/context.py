import json
import re

__version__ = "0.3.0"


def assign_value_to_variable(var, var_key, var_value=None, is_assign=False):
    if type(var) is not dict:
        var = dict()

    if is_assign:
        var[var_key] = var_value
    else:
        if var_key not in var:
            var[var_key] = dict()

    return var[var_key]


def parse_var_name(var_name):
    return var_name.split('[', 1)[0], re.findall(r'\[([а-яА-Яa-zA-Z0-9_]+)]', var_name)


class Context:
    variables = dict()

    def set(self, var_name, var_value):
        main, add = parse_var_name(var_name)
        len_add = len(add)

        var = assign_value_to_variable(self.variables, main)

        for c, r in enumerate(add, 1):
            if len_add == c:
                var = assign_value_to_variable(var, r, var_value, True)
            else:
                var = assign_value_to_variable(var, r)

    def get(self, var_name):
        main, add = parse_var_name(var_name)
        var = None
        if main in self.variables:
            var = self.variables[main]
            for n in add:
                var = var.get(n)
        return var


if __name__ == "__main__":
    context = Context()
    context.set('Услуги[0][Специалисты][0][ФИО]', "Соколова Алиса Андреевна")
    context.set('Услуги[1][Имя]', "Педикюр")

    # main, add = parse_var_name('Услуги[)]')
    # print(main)
    # print(add)

    print(json.dumps(context.variables, ensure_ascii=False, indent=True))

    print(context.get('Услуги[0][Специалисты]'))
    print(context.get('Услуги'))

    # print(context.variables.get('Услуги').get('1'))
    # print(context.variables)
