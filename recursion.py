# Write a Python program to calculate the sum of a list of numbers. 
def summ(l):
    if len(l) == 1:
        return l[0]

    else:
        return l[0] + summ(l[1:])

l = [4,6,8,12,7,9]
print(summ(l)) 
