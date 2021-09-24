#Write a program to display only those numbers from a list that satisfy the following conditions

""" 1. The number must be divisible by five
    2. If the number is greater than 150, then skip it and move to the next number
    3. If the number is greater than 500, then stop the loop """

numbers = [12, 75, 150, 180, 145, 525, 50]

for n in numbers:
    if n%5==0:
        if 500>n>150:
            continue
        elif n>500:
            break
        else:
            print(n)