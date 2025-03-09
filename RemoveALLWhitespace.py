#Removing All WhiteSpace in a String
import re

string = "C  O  D  E"  # String with multiple spaces
space = re.compile(r'\s+')  # Matches one or more whitespace characters
result = re.sub(space, "", string)  # Replaces all matched spaces with an empty string
print(result)
""" re.compile(r'\s+'):

Compiles a regular expression pattern that matches one or more whitespace characters (\s+).
re.sub(space, "", string):

Replaces all occurrences of the pattern (extra spaces) with an empty string ("").
print(resul"""





#(3) Method
string = "C  O  D  E"
result = string.replace(" ", "")  # Replace all spaces with an empty string
print(result)


