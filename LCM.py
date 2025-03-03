a=int(input("Enter the first number: "))
b=int(input("Enter the second number: "))
if a==b:
    print("LCM i",b)
else:
    if a>b:
        max=a
    else:
        max=b
    i=max
    while(1):
        if(max%a==0 and max%b==0):
            print("LCM is",max)
            break
        else:
            max=max+i
