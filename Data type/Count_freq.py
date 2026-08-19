text = input("Enter a string: ")

choice = input("Ignore case? (yes/no): ")

# Convert to lowercase if user chooses ignore case
if choice == "yes":
    text = text.lower()


# Count frequency of each character
frequency = {}

for ch in text:
    if ch in frequency:
        frequency[ch] += 1
    else:
        frequency[ch] = 1


# Display frequency in descending order
print("\nCharacter Frequency:")

while len(frequency) > 0:

    highest_char = ""
    highest_frequency = 0

    for ch in frequency:
        if frequency[ch] > highest_frequency:
            highest_frequency = frequency[ch]
            highest_char = ch

    if highest_char == " ":
        print("Space :", highest_frequency)
    else:
        print(highest_char, ":", highest_frequency)

    del frequency[highest_char]