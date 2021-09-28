# Remove Tuples of Length K.

l = [(1,),(2,4),(3,6,7),(5,7),(3,),(6,5,3)]

k = int(input("Enter the length of tuple to be removed: "))

res = [ element for element in l if len(element) != k]

print(res)