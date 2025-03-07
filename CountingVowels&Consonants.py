#Counting VOWELS in a Given Word
vowel=['a','e','i','o','u']
word="programming"
count=0
for character in word:
    if character in vowel:
        count+=1
print(count)

#Counting CONSONANTS i a given word
vowel=['a','e','i','o','u']
word=input("Enter the String word:-")
count=0
for character in word:
    if character not in vowel:
        count+=1
print(count)
