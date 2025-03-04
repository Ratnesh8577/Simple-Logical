# Leap Year
year=int(input("Enter the years: "))
if (year%400==0):
    print("Leap Year")
elif (year%4==0 and year%100!=0):
    print("Leap Year")
else:
    print("Not Leap year")