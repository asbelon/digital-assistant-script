import json

from flask import Flask, jsonify

from context.context import Context, parse_var_to_list

# from context.context import Context, parse_var_to_list

app = Flask(__name__)


@app.route("/specialists", methods=['POST'])
def get_specialists():
    with open('./context.json', encoding='utf-8') as f:
        context = Context(json.load(f))
        specialist_list = parse_var_to_list(context.variables)
    return jsonify(specialist_list)


@app.route("/specialist/date_list", methods=['POST'])
def get_date_list():
    date_list = [
        {
            "name": "ДоступныеДаты[0]",
            "value": "28 сентября"
        },
        {
            "name": "ДоступныеДаты[1]",
            "value": "29 сентября"
        }
    ]
    return jsonify(date_list)


if __name__ == "__main__":
    app.run()
