#Counting the number of occurance of a character in a string
word=input("Enter the String word:-")
character=input("Enter the one character word:-")
#count the letter in word
count=0
for i in word:
    if i==character:
        count+=1
print(count)