import csv

with open('pincode.csv',newline='') as file:
      reader= csv.reader(file)
      for row in reader:
            print(row)
      fields=['circlename','pincode']
      writer=csv.DictWriter(file,filednames=fields)
      writer.writeheader()
