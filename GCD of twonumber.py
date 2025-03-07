num1=int(input("Enter 1st number: "))
num2=int(input("Enter 2st number: "))
def gcd(a,b):
    if a==0 or a==b:
        return b
    elif b==0:
        return a 
    elif a>b:
        return gcd(a-b,b)
    return gcd(a,b-a)
gcd(num1,num2)