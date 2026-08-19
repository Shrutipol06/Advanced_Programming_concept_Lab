text = input("Enter a paragraph: ")

# Convert text to lowercase
text = text.lower()

# Split paragraph into words
words = text.split()

# Count total words
total_words = len(words)

print("\nTotal number of words:", total_words)


# Create dictionary for word frequency
frequency = {}

for word in words:
    if word in frequency:
        frequency[word] += 1
    else:
        frequency[word] = 1

# Display word frequency
print("\nWord Frequency:")

for word in frequency:
    print(word, ":", frequency[word])


# Find top 3 most frequent words
temp = frequency.copy()

print("\nTop 3 most frequent words:")

for i in range(3):
    if len(temp) == 0:
        break

    highest_word = ""
    highest_frequency = 0

    for word in temp:
        if temp[word] > highest_frequency:
            highest_frequency = temp[word]
            highest_word = word

    print(highest_word, ":", highest_frequency)

    del temp[highest_word]


# Count vowels
vowels = "aeiou"
vowel_count = 0

for ch in text:
    if ch in vowels:
        vowel_count += 1

print("\nNumber of vowels:", vowel_count)