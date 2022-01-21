 = ['add', 'sub', 'div', 'mult']


def add(num1, num2):
    return num1 + num2


def sub(num1, num2):
    return num1 - num2


def div(num1, num2):
    return "Can't divide by zero mate" if num2 == 0 else num1 / num2


def mult(num1, num2):
    return num1 * num2


def calculator(num1, num2, operator):
    if operator not in operators:
        print('Wrong operator, please choose from: {0}'.format(operators))

    if operator == 'add':
        print(add(num1, num2))
    if operator == 'sub':
        print(sub(num1, num2))
    if operator == 'div':
        print(div(num1, num2))
    if operator == 'mult':
        print(mult(num1, num2))


calculator(1, 2, 'add')
calculator(1, 2, 'sub')
calculator(1, 0, 'div')
calculator(1, 2, 'mult')
