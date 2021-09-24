# Write a program to display all prime numbers within a range.

s = int(input("Enter starting number: "))
e = int(input("Enter ending number: "))


for i in range(s,e+1):
    for j in range(2,i):
        if i%j==0:
            break
    else:
        print(i)
