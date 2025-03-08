#Write a Python Program to calculate the natural logarithm of any number

import math
num = float(input("Enter a number: "))
if num <= 0:
    print("Please enter a positive number.")
else:
    #Calcutate the natural Logarithm (base e ) of the number
    result = math.log(num)
    print(f"The natural logarithm of {num} is: {result}")
    