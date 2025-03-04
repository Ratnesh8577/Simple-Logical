# SPY Number:-A number is said to be a spy number if sum of its is equal to the product of  digits
n=int(input("Enter the Number: "))
a=n
sum=0
product=1
while (n>0):
    b=n%10
    sum=sum+b
    product=product*b
    n=n//10
if sum==product:
    print("This number is SPY Number")
else:
    print("Not a SPY number")