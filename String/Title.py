s = input("Enter a sentence: ")

result = ""
new_word = True

for ch in s:
    if ch == " ":
        result += ch
        new_word = True
    else:
        if new_word:
            result += ch.upper()
            new_word = False
        else:
            result += ch

print(result)