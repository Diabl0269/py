import uuid
from db import *


class Model(object):
    def __init__(self, entity={}):
        if 'id' in entity:
            data = convert_data(read_db())
            if entity['id'] in data:
                self.entity = data[entity['id']]
                return
        self.entity = entity
        self.generate_id()

    # Creates the entry in the DB
    def create(self):
        output = read_db()
        if len(output) == 0:
            init_db(self.entity)
        else:
            data = convert_data(output)
            data[self.entity['id']] = self.entity
            write_to_db(data)

    def update(self, updates):
        for key in updates:
            self.entity[key] = updates[key]
        self.save()

    # Saves the entry in the DB after an update
    def save(self):
        output = read_db()
        if len(output) == 0:
            if 'id' not in self.entity:
                self.generate_id()
            init_db(self.entity)
        else:
            data = convert_data(output)
            data[self.entity['id']] = self.entity
            write_to_db(data)

    def generate_id(self):
        self.entity['id'] = str(uuid.uuid4())

    def delete(self):
        output = read_db()
        if len(output) == 0:
            return
        data = convert_data(output)
        del data[self.entity['id']]
        write_to_db(data)


# Examples
if __name__ == '__main__':
    m = Model({"name": "Tal"})
    m.create()
    db = read_db()
    print(db)
    m.update({"name": "Efronny"})
    db = read_db()
    print(db)
    m.delete()
    db = read_db()
    print(db)

    m = Model({"name": "Rotem"})
    m.create()

    print("Done")
    db = get()
    print(db)
