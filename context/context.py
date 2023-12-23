import json
import re
from pathlib import Path
from typing import Any

pattern = re.compile(r'\[([а-яА-Яa-zA-Z0-9_]+)]')


def assign_value_to_variable(var: dict, var_key: str, var_value=None, is_assign=False):
    if not var:
        var = dict()

    if is_assign:
        var[var_key] = var_value
    else:
        if var_key not in var:
            var[var_key] = dict()

    return var[var_key]


def parse_var_name(var_name):
    return var_name.split('[', 1)[0], pattern.findall(var_name)


def create_var_name(path):
    name = path.pop(0)
    for p in path:
        name = f'{name}[{p}]'
    return name


def parse_var_to_list(var: dict | str | int, path: list = None):
    if path is None:
        path = []

    if isinstance(var, dict):
        for k in var:
            copied_path = path.copy()
            copied_path.append(k)
            yield from parse_var_to_list(var[k], copied_path)
    else:
        yield {
            "name": create_var_name(path),
            "value": var
        }


class ContextError(Exception):
    pass


class ParseError(ContextError):
    pass


class Context:
    variables: dict

    def __init__(self, variables: dict | None = None, ctx: "Context" = None):
        self.parent = ctx
        if isinstance(variables, dict):
            self.variables = variables
        else:
            self.variables = dict()

    @classmethod
    def load_from_file(cls, file_path: str | Path):
        """Загрузить из файла"""
        try:
            with open(file_path, "r", encoding='utf-8') as f:
                data = json.load(f)
        except json.JSONDecodeError as e:
            raise ParseError('Parse error') from e
        return cls(data)

    def dump_to_file(self, file_path: str | Path, **kwargs):
        """Сохранить в файл"""
        with open(file_path, "w", encoding='utf-8') as f:
            json.dump(self, f, ensure_ascii=False, indent=4, default=str, **kwargs)

    def set(self, var_name, var_value):
        main, add = parse_var_name(var_name)
        len_add = len(add)

        var = assign_value_to_variable(self.variables, main)

        for c, r in enumerate(add, 1):
            if len_add == c:
                var = assign_value_to_variable(var, r, var_value, True)
            else:
                var = assign_value_to_variable(var, r)

    def get(self, var_name, default=None):
        main, add = parse_var_name(var_name)
        try:
            var = self.variables[main]
            for n in add:
                var = var.get(n)
        except KeyError:
            return default
        else:
            return var

    def __iter__(self):
        return parse_var_to_list(self.variables)

    def __getitem__(self, name: str):
        return self.get(name)

    def __setitem__(self, name: str, value: Any):
        self.set(name, value)


if __name__ == "__main__":
    with open('./context.json', encoding='utf-8') as f:
        context = Context(json.load(f))
        vars_list = parse_var_to_list(context.variables)
        # print(json.dumps(vars_list, ensure_ascii=False, indent=True))
        # print(json.dumps(context.variables, ensure_ascii=False, indent=True))

        with open('./variable.json', 'w', encoding='utf-8') as outfile:
            json.dump(vars_list, outfile, ensure_ascii=False, indent=4)
            context_reload = Context()

            for v in vars_list:
                context_reload.set(v.get("name"), v.get("value"))
            with open('./context_reload.json', 'w', encoding='utf-8') as file:
                json.dump(context_reload.variables, file, ensure_ascii=False, indent=4)
