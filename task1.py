import csv

salesTax = 20
i_file = input("Enter a csv file: ")

with open(i_file,'r') as n:
    csv_reader = csv.DictReader(n)

    
    with open('result.csv','w') as m:
        fieldnames = ['Product-name','Product-CostPrice','Country','Product-Salestax','Product-Finalprice']
        csv_writer = csv.DictWriter(m,fieldnames=fieldnames)

        csv_writer.writeheader()


    
with open(i_file,'r') as o:
    csv_read = csv.reader(o)
    next(csv_read)


    with open('result.csv','a') as p:
        csv_w = csv.writer(p)
    
        for line in csv_read:
            finalPrice = int(line[1]) + int(line[1])*salesTax/100
            csv_w.writerow([line[0],line[1],line[2],salesTax,finalPrice])
            
 