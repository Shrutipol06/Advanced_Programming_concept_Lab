s1 = input("Enter first string: ")
s2 = input("Enter second string: ")

# Create dictionaries
freq1 = {}
freq2 = {}

# Process first string
for ch in s1:
    if ch != " ":
        if ch >= 'A' and ch <= 'Z':
            ch = chr(ord(ch) + 32)

        if (ch >= 'a' and ch <= 'z') or (ch >= '0' and ch <= '9'):
            if ch in freq1:
                freq1[ch] += 1
            else:
                freq1[ch] = 1


# Process second string
for ch in s2:
    if ch != " ":
        if ch >= 'A' and ch <= 'Z':
            ch = chr(ord(ch) + 32)

        if (ch >= 'a' and ch <= 'z') or (ch >= '0' and ch <= '9'):
            if ch in freq2:
                freq2[ch] += 1
            else:
                freq2[ch] = 1


# Compare dictionaries
if freq1 == freq2:
    print("The strings are anagrams.")
else:
    print("The strings are not anagrams.")