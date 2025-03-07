#Comparing Two Strings for ANAGRAMS
str1="Listen"
str2="Silent"

str1=str1.replace(" "," ").upper()
str2=str2.replace(" "," ").upper()

if sorted(str1)==sorted(str2):
    print("True")
else:
    print("False")


    