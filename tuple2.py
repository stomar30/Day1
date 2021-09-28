# Sort list of tuple by second item.

l = [(1,0),(2,4),(3,6,7),(5,7),(3,9),(6,5,3)]

for i in range(len(l)):
    for j in range(len(l)):
        if l[i][1] < l[j][1]:
            temp = l[i]
            l[i ]= l[j]
            l[j] = temp

print(l)