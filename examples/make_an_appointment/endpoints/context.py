import re
from hashlib import md5

__version__ = "0.1.0"


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
    dictionary = dict()

    def set_to_dictionary(self, var_name):
        var_key = md5(var_name.encode('utf-8')).hexdigest()
        if var_key not in self.dictionary:
            self.dictionary[var_key] = var_name
        return var_key

    def set(self, var_name, var_value):
        parts = var_name.split('[', 1)
        is_complex = len(parts) > 1
        main = parts[0]

        # k = self.set_to_dictionary(main)
        var = assign_value_to_variable(self.variables, main)

        if is_complex:
            result = re.findall(r'\[([а-яА-Яa-zA-Z0-9_]+)]', var_name)
            result_length = len(result)
            for c, r in enumerate(result, 1):
                # k = self.set_to_dictionary(r)
                if result_length == c:
                    var = assign_value_to_variable(var, r, var_value, True)
                else:
                    var = assign_value_to_variable(var, r)


if __name__ == "__main__":
    context = Context()
    context.set('Услуги[0][Специалисты][0][ФИО]', "Соколова Алиса Андреевна")
    print(context.variables)
