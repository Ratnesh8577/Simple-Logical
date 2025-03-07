#Counting Digits,Letters,and Space in a String
def count_chars(s):
    digits=0
    letters=0
    spaces=0
    for char in s:
        if char.isdigit():
            digits+=1
        elif char.isalpha():
            letters+=1
        elif char.isspace():
            spaces+=1
    return digits,letters,spaces

#Driver code
text=input("Enter the string:-")
digits,letters,space=count_chars(text)
print(f"Digits:{digits},Letters:{letters},Space:{space}")

#Output:-
#Enter the string:-ffsgftytf
#Digits:0,Letters:9,Space:0

#(2) Method
def count_characters(s):
    digits = sum(c.isdigit() for c in s)
    letters = sum(c.isalpha() for c in s)
    spaces = sum(c.isspace() for c in s)
    return digits, letters, spaces

# Example usage:
text = input("Enter a string: ")
digits, letters, spaces = count_characters(text)
print(f"Digits: {digits}, Letters: {letters}, Spaces: {spaces}")

#output
"""Enter a string: Hello World 123
Digits: 3, Letters: 10, Spaces: 2
"""


import re

name = 'Python is 1'

digitCount = re.sub("[^0-9]", "", name)  # Retains only digits
letterCount = re.sub("[^a-zA-Z]", "", name)  # Retains only letters
spaceCount = re.findall("[\s]", name)  # Finds all spaces

print(len(digitCount))  # Count of digits
print(len(letterCount))  # Count of letters
print(len(spaceCount))  # Count of spaces
