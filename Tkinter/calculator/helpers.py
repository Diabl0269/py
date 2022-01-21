class Calculator(object):
    def __init__(self):
        self.operator = ''
        self.num1 = ""
        self.num2 = ""
        self.result = ""
        # False - num1, True - num2
        self.current_input = False

    def __call__(self, *args, **kwargs):
        operator = self.operator
        num1 = int(self.num1)
        num2 = int(self.num2)
        result = 0
        print(self.operator)
        if operator == '+':
            result = num1 + num2
        if operator == '-':
            result = num1 - num2
        if operator == '/':
            result = num1 / num2
        if operator == '*':
            result = num1 * num2

        self.result = str(result)
        self.num1 = ''
        self.num2 = ''
        self.current_input = False

    def handle_operator(self, operator):
        self.operator = operator

    def handle_input(self, num):
        if self.current_input:
            self.num1 += num
        else:
            self.num2 += num

    def clear(self):
        self.result = ""
        self.num1 = ""
        self.num2 = ""
