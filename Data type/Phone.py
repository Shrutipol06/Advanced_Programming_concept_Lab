import re

def extract_phone_numbers(text):
    pattern = r'(\(\d{3}\)\s\d{3}-\d{4}|\d{3}-\d{3}-\d{4}|\d{3}\.\d{3}\.\d{4}|\d{10})'

    numbers = re.findall(pattern, text)

    return numbers


text = input("Enter text: ")

phone_numbers = extract_phone_numbers(text)

print("Phone numbers found:")

for number in phone_numbers:
    print(number)