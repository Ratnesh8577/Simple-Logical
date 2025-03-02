#       Palindrome
# Palindrome:-A number which is same from left and right is a
#  -Palindrome number
n=int(input("Enter the number: "))
sum=0
a=n
while(n>0):
    b=n%10
    sum=(sum*10)+b
    n=n//10
if sum==a:
    print("Palindrome")
else:
    print("Not Palindrome")
