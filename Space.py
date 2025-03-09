
#Counting the white Space & word counting
string="Ratnesh chauhan  "
print(string.count("R"))

#output:-1

#(1)
def count_whitespace(s):
    return s.count(" ")  # Count the number of spaces

# Example usage:
text = input("Enter a string: ")
whitespace_count = count_whitespace(text)
print(f"The string contains {whitespace_count} white space(s).")


