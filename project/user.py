from model import Model
from db import *


class User(Model):
    def __init__(self, first_name='', last_name='', _id=''):
        if len(_id) > 0:
            data = convert_data(read_db())
            if _id in data:
                self.entity = data[_id]
                return
        self.entity = {"first_name": first_name, "last_name": last_name}
        self.generate_id()


if __name__ == '__main__':
    user = User('Tal', "Efronny")
    user.create()

    output = get()
    print(output)
