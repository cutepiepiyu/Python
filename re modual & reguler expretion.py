import re

"""searching for pattern"""
txt="cyber security lab 2025."
if re.search(r'\d',txt):
    print("1. the string contain number.")
else:
    print("1. the string does not contain number.")


"""Extracting Emails."""
txt = "Please contact us at jigna123@gmail.com or priya@gmail.com for more information."
emails = re.findall(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b', txt)
print("2. Extracted emails:", emails)


"""Validating Phone Numbers."""
phone="123-456-7890"
if re.fullmatch(r'\d{10}', phone):
    print("3. Valid phone number.")
else:
    print("3. Invalid phone number.")


"""Finding Capitalized Words."""
sentence = "Python is fun and Important."
capitalized_words = re.findall(r'\b[A-Z][a-z]*\b', sentence)
print("4. Capitalized words:", capitalized_words)


"""Replacing Digits."""
text="Server123 has IP 456."
replace=re.sub(r'\d', '#', text)
print("5. Replaced digits:", replace)


""""""