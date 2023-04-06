# Calculate Func
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


# Variables
out = None

num1 = int(input("Enter your first number = "))
expression = input("Enter expression = ")
num2 = int(input("Enter your first number = "))

print("The answer is = " + str(calculate()))
