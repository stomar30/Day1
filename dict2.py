# Python – Replace String by Kth Dictionary value.
l = ["Gfg", "is", "Best"]

d = { "Gfg" : [5, 6, 7], "is" : [7, 4, 2]}
K = 2

res = [ele if ele not in d else d[ele][K]
									for ele in l]
		
print("The list after substitution : " + str(res))
