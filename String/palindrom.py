s="level"
reverse=""
for ch in s:
    reverse=ch+reverse
if s==reverse:
    print("string is a palindrom")
else:
    print("string is not palindrom")