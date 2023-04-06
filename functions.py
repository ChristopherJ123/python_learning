x = "I am a variable"


def name():
    x = "Christopher Joshua"
    print(x)


def age():
    x = 18
    print(x)


def bloodtype():
    global x
    x = 'O'
    print(x)


name()
age()
bloodtype()
print(x)
