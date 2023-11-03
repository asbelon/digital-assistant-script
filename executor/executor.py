import json
from urllib.request import urlopen


class Scenario:
    id = ''
    name = ''
    commands = dict()
    base_url = ''

    def __init__(self, scenario_description, base_url=None):
        if base_url:
            self.base_url = base_url
        if type(scenario_description) is dict:
            self.id = scenario_description.get('id')
            self.name = scenario_description.get('name')
            commands = scenario_description.get('commands')
            for command in commands:
                self.commands[command.get('name')] = self.load_sequence(command.get('sequence'))

    def load_sequence(self, info):
        if info is dict:
            pass
        elif info is str:
            pass

        return ''
        # self.commands[command.get('name')] = sequence


class Executor:
    pass


def get_jsonparsed_data(url):
    """
    Receive the content of ``url``, parse it as JSON and return the object.

    Parameters
    ----------
    url : str

    Returns
    -------
    dict
    """
    response = urlopen(url)
    # print(response.read().decode("utf-8"))
    data = response.read().decode("utf-8")
    return json.loads(data)


if __name__ == "__main__":
    base = 'https://schema.proxila.ru/make_an_appointment/'
    url = base + '1d44f96e-712d-415d-b12a-188c0529a412.scenario.json'
    description = get_jsonparsed_data(url)
    print(description)
    # s = Scenario(description)
    # print(s.name)
    # print(s.commands)
