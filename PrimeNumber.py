#Write a python Program to Check Prime Number
num= int(input("Enter a number: "))
#define a flag variable
flag = False
if num == 1:
    print(f"{num},is not a prime number")
elif num>1:
    #check for factors
    for i in range(2,num):
        if (num % i )==0:
            flag=True #if factor is found set flag to true
            #break out of loop
            break
        #check if flag is true
if flag:
    print(f"{num}, is not a prime number")
else:
    print(f"{num},is a prime number")

#Enter a number: 5
# 5,is a prime number