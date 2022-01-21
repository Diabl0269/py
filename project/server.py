from flask import Flask, request
from db import *
from config import *
from user import User

# Initialize
app = Flask("Database manager")


@app.get(GET_USERS)
def get_data():
    data = read_db()
    print(data)
    return data


@app.post(CREATE_USER)
def create_user():
    first_name = request.json['first_name']
    last_name = request.json['last_name']
    user = User(first_name, last_name)
    user.create()
    return "Created"


@app.put(UPDATE_USER)
def update_user():
    user = User(_id=request.json['id'])
    user.update(request.json)
    return "Updated"


@app.delete(DELETE_USER)
def delete_user():
    _id = request.args.get('id')
    user = User(_id=_id)
    user.delete()
    return "Deleted"


if __name__ == '__main__':
    app.run("127.0.0.1", port=PORT, debug=True)
