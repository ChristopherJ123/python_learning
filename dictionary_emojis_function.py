emojis = {
    ":)": "🙂",
    ":(": "🙁"
}


def emoji(text):
    output = ""
    for word in text:
        output += f"{emojis.get(word, word)} "
    return output


user_input = input("Write something\n")
print(emoji(user_input.split()))
