from calculator import num1, num2, expression


def calculate():
    global out
    if expression == '+':
        out = num1 + num2
    elif expression == '-':
        out = num1 - num2
    elif expression == '*':
        out = num1 * num2
    elif expression == '/':
        out = num1 / num2
    elif expression == '//':
        out = num1 // num2
    elif expression == '%':
        out = num1 % num2
    elif expression == '^':
        out = num1 ** num2

    if str(out).endswith('.0'):
        return str(out[:-2])
    else:
        return out
