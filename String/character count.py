s="shruti @2"
vowels = 0
consonants = 0
digit = 0
spaces = 0
special = 0
for ch in s:
    if ch.lower() in "aeiou":
        vowels+=1
    elif ch.isalpha():
        consonants+=1
    elif ch.isdigit():
        digit+=1
    elif ch ==" ":
        spaces+=1
    else:
        special+=1
print("vowels:",vowels)
print("consonants:",consonants)
print("digits:",digit)
print("space:",spaces)
print("special:",special)
