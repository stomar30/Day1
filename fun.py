""" Write a Python program that accepts a hyphen-separated sequence of 
    words as input and prints the words in a hyphen-separated sequence 
    after sorting them alphabetically. """

def sort_s(s):
    s =  s.split("-")
    for i in range(0,len(s)):
        for j in range(0,len(s)):
            if s[i] < s[j]:
                temp = s[i]
                s[i] = s[j]
                s[j] = temp

    print("-".join(s))


s = input("Enter the Hypen seperated words: ")

sort_s(s)