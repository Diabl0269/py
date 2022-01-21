import os
import re

numOfCommands = 5


def run_commands():
    print("Please insert {0} commands".format(numOfCommands))
    commands = []

    for i in range(5):
        commands.append(input("Insert a command:"))

    for command in commands:
        os.system(command)

    print("Finished running commands :)")


def get_ip():
    ip = os.popen("ifconfig | grep broadcast | cut -d ' ' -f 2").read()
    print("Your ip is: {0}".format(ip))
    return ip


if __name__ == "__main__":
    get_ip()
