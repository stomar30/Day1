# Write a Python program of recursion list sum.

def list_sum(l):
    total = 0
    for i in l:
        if type(i) == type([]):
            total = total + list_sum(i)

        else:
            total = total + i

    return total



l = [1, 2, [3,4], [5,6]]
print(list_sum(l))