# Python program to find the sum of all items in a dictionary.


def summ(myDict):
	
	list = []
	for i in myDict:
		list.append(myDict[i])
	final = sum(list)
	
	return final

dict = {'a': 100, 'b':200, 'c':300}
print("Sum :", summ(dict))
