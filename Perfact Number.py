#A number is said to be perfact number if sum of its factors (Excluding that
# number as a factor) is equal to the number
n= int(input("Enter teh number: "))
sum=0
i=1
while(i<=(n//2)):
    if n%i==0:
        sum=sum+i
        i=i+1
if sum==n:
    print("Perfect Number")
else:
    print("Not a perfect number")