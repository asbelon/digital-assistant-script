from flask import Flask, jsonify

app = Flask(__name__)


@app.route("/specialists", methods=['POST'])
def get_specialists():
    specialist_list = [
        {
            "name": "Услуги[0][Имя]",
            "value": "Консультация"
        },
        {
            "name": "Услуги[0][Стоимость]",
            "value": "500 р"
        },
        {
            "name": "Услуги[0][Специалисты][0][ФИО]",
            "value": "Соколова Алиса Андреевна"
        },
        {
            "name": "Услуги[0][Специалисты][1][ФИО]",
            "value": "Сорокина Василиса Фёдоровна"
        },
        {
            "name": "Услуги[1][Имя]",
            "value": "Педикюр"
        },
        {
            "name": "Услуги[1][Стоимость]",
            "value": "от 700 р"
        },
        {
            "name": "Услуги[1][Специалисты][0][ФИО]",
            "value": "Константинова Елизавета Григорьевна"
        },
        {
            "name": "Услуги[1][Специалисты][1][ФИО]",
            "value": "Николаева Ника Максимовна"
        },
        {
            "name": "Услуги[2][Имя]",
            "value": "Маникюр"
        },
        {
            "name": "Услуги[2][Стоимость]",
            "value": "от 800 р"
        },
        {
            "name": "Услуги[2][Специалисты][0]",
            "value": "Евдокимова Ульяна Ильинична"
        }
    ]
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
