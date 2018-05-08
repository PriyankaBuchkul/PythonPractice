import csv
n=0
with open('pincode.csv',newline='') as f:
      spamreader=csv.reader(f,delimiter=',',quotechar='|')
      f1=open('data_csv1.txt','w+')
      for row in spamreader:
            for i in row:
                  if i=='Maharashtra':
                        #l=i.split(',')[:2]
                        print(row[1]+' '+row[6])
                        break
      
      
           
      
