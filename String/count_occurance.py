s = input("Enter a sentence: ")
word = input("Enter word: ")

count = 0
current = ""

for ch in s + " ":
    if ch != " ":
        current += ch
    else:
        if current == word:
            count += 1
        current = ""

print("Count:", count)