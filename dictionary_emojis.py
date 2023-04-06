user_input = input()
words = user_input.split()
emojis = {
    ":)": "🙂",
    ":(": "🙁"
}
output = ""
for word in words:
    output += f"{emojis.get(word, word)} "
print(output)
