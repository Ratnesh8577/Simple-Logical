#Swap two variable
num1=int(input("Enter the first number: "))
num2=int(input("Enter the second value: "))
'''temp=num1
num1=num2
num2=temp'''
num1=num1+num2
num2=num1-num2
num1=num1-num2
print(num1,num2)