# Remove duplicate lists from the tuple.

l = ([3],[2,4],[3,6,7],[5,7],[3],[6,7,3],[2,4])

j = list(l)

res = []
for element in j:
    if element not in res:
        res.append(element)

print(tuple(res))
