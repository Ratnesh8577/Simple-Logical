#Write a Python Program to KPrint all Number in an Interval of 1-10
lower=1
upper=10

for num in range(lower,upper+1):
    if num>1:
        for i in range(2,num):
            if (num%i)==0:
                break
        else:
            print(num)
"""
#OUTPUT
#2
3
5
7
"""