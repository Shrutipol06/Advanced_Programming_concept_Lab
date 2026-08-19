# Take input for two books

book1 = input("Enter text of Book 1: ")
book2 = input("Enter text of Book 2: ")

# Convert text into words
words1 = book1.lower().split()
words2 = book2.lower().split()

# Convert lists into sets to get unique words
set1 = set(words1)
set2 = set(words2)

# Common words
common = set1 & set2

# Words unique to Book 1
unique_book1 = set1 - set2

# Words unique to Book 2
unique_book2 = set2 - set1

# All unique words
all_words = set1 | set2

# Display results
print("\nUnique words in Book 1:")
print(set1)

print("\nUnique words in Book 2:")
print(set2)

print("\nCommon words:")
print(common)

print("\nWords unique to Book 1:")
print(unique_book1)

print("\nWords unique to Book 2:")
print(unique_book2)

print("\nTotal unique words across both books:")
print(len(all_words))