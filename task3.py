from taxModule import *


print("Welcome To TAX CALCULATOR")
i_file = input("Enter a csv file: ")


obj = Calculation(i_file) 
obj.taxCalculation()
print("DONE")