# Python program to check if a string has at least one letter and one numberdef checkString(str):
	
def checkString(str):
	
	flag_l = False
	flag_n = False
	
	for i in str:
		if i.isalpha():
			flag_l = True
        if i.isdigit():
			flag_n = True
	
	return flag_l and flag_n


print(checkString('thishasboth29'))
print(checkString('geeksforgeeks'))

