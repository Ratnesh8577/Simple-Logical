#(1)
"""def fib(n):
    if n<=1:
        return 1
    else:
        return fib(n-1)+fib(n-2)
#Driver code 
n=int(input("Enter the fib number:-"))
result=fib(n)
print("Fibonacci Series",result)"""



#(2)
fib = [0,1]
#Range stars from 0 by default
n=int(input("Enter the number of fibonacci:-"))
for i in range(n):
    fib.append(fib[-1] + fib[-2])
#Converting the List of integer to string
print(','.join(str(e) for e in fib))






