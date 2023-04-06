numbers = {
    1: "one",
    2: "two",
    3: "three",
    4: "four",
    5: "five",
    6: "six",
    7: "seven",
    8: "eight",
    9: "nine",
    0: "zero"
}

phone_number = {"Phone number": input("Phone number: ")}

phone_number_word = ""
for number in phone_number["Phone number"]:
    phone_number_word += f"{numbers[int(number)]} "
print(phone_number_word)
