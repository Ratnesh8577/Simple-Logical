#Write a Python Program to Find LCM(Least Commaon Multiple)
#LCM(a,b)== |a,b|/GCD(a,b)
# GCD stands for Greatest Common Divisor

#Python Program to find the LCm of two input number
def compute_lcm(x,y):
    if x > y:           #choose the greater number
                    
        greater = x
    else:
        greater = y   #choose the greater number  
    while (True):
        if ((greater % x == 0) and (greater % y == 0)):
            lcm=greater
            break
        greater+=1
    return lcm





#Driver code
num1=int(input("Enter the number: "))
num2=int(input("Enter the number:"))
print("The L.C.M is ",compute_lcm(num1,num2))