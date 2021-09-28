# Python program for removing i-th character from a string.

def remove(string, i):

	a = string[ : i]
	b = string[i + 1: ]
	
	return a + b
	
	
string = "geeksFORgeeks"
	
i = 5
	
print(remove(string, i))
