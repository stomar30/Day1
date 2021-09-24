# Write a Python program that accepts a word from the user and reverse it.

s =""
word = input("Enter word: ")

for i in range (len(word)-1,-1,-1):
    s+=word[i]
   

print(s)