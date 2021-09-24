"""Take integer inputs from user until he/she presses q ( Ask to press 
q to quit after every integer input ). Print average and product of all 
numbers. """
n = "a"
sum = 0
pro = 1
count = 0
while n!="q":
    i = int(input("Enter a number: "))
    sum+=i
    count+=1
    pro*=i
    n = input("Press q to quit or c to continue: ")
    if n == "c":
        continue

print("Average: ",sum/count)
print("prodct: ", pro)


    


