#Write a Python Program tu Find the SUm of Natural Numbers.
# N=1,2,3,4,5,67,.......

limit = int(input("Enter the limit: "))
#Intialize the sum (blank sum)
sum=0
for i in range(1,limit+1):
    #sum =sum+i
    sum+=i
print("The sum of nutural numbers up to ",limit,"is:",sum)