import json
from helpers import format_json


def read_db():
    with open('db.json', 'r') as f:
        return str(f.read())


def write_to_db(data):
    with open('db.json', 'w') as f:
        f.truncate()
        f.write(format_json(data))


def get():
    with open('db.json', 'r') as f:
        return json.loads(str(f.read()))


def init_db(entity):
    with open('db.json', 'w') as f:
        f.write(json.dumps({entity['id']: entity}))


def convert_data(output):
    return json.loads(str(output))
