#Armstrong Number:-A number is said to be armstronge number 

#if the sum of its digits raised to their power of number of digit of 

#number is equal to the number

n=int(input("Enter the number: "))
k=n
a=n
count=0
while(n>0):
    count=count+1
    n=n//10

sum=0
while(a>0):
    b=a%10
    sum=sum+pow(b,count)
    a=a//10
if sum==k:
    print("Armstrong")
else:
    print("Number is not Armstrong")