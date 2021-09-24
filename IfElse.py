#Write a program to calculate the electricity bill (accept number of unit from user) according to the following criteria :
"""   Unit                   Price  
First 100 units           no charge
Next 100 units           Rs 5 per unit
After 200 units          Rs 10 per unit   """


unit = int(input("Enter number of units: "))

if unit <= 100:
    print("No Charge")

elif 200 >= unit > 100:
    bill = unit*5
    print(bill)

else:
    bill = unit*10
    print(bill)
