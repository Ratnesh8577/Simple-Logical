#Find the Maximum Number in a list
numberlist=[12,33,1,4,55,3,75,32,45,21]
max=numberlist[0]
for i in (numberlist):
    if max<i:
        max=i
print(max)

#Find the Minimum Number in a list
numberlist=[12,33,1,4,55,3,75,32,45,21]
min=numberlist[0]
for i in (numberlist):
    if min > i:
        min=i
print(min)