sentence = input("Enter a sentence: ")

longest = ""

for word in sentence.split():
    if len(word) > len(longest):
        longest = word

print("Longest word:", longest)