import json
import requests
from config import *
from helpers import format_json

headers = {'Content-type': 'application/json'}
BASE_URL = "{0}:{1}".format(IP, PORT)


def create_user():
    first_name = input("Please inset the first name. ")
    last_name = input("Please inset the last name. ")
    return requests.post("{0}{1}".format(BASE_URL, CREATE_USER),
                         json={"first_name": first_name, "last_name": last_name},
                         headers=headers).text


def get_data():
    return format_json(requests.get("{0}{1}".format(BASE_URL, GET_USERS)).json())


def update_user():
    _id = input("Insert an id to update.")
    update_key = input("Insert the key to update. (first_name | last_name) ")
    update_value = input("Insert the new value. ")
    return requests.put("{0}{1}".format(BASE_URL, UPDATE_USER),
                        json={"id": _id, update_key: update_value},
                        headers=headers).text


def delete_user():
    _id = input("Insert an id to delete. ")
    return requests.delete("{0}{1}".format(BASE_URL, DELETE_USER),
                           params={"id": _id}).text


if __name__ == '__main__':
    print("Welcome")
    while True:
        inp = input("Please choose a command:"
                    "\n1: Create user."
                    "\n2: Get database."
                    "\n3: Update record."
                    "\n4: Delete user.\n")
        if inp == '1':
            print(create_user())
        if inp == '2':
            print(get_data())
        if inp == '3':
            print(update_user())
        if inp == '4':
            print(delete_user())
