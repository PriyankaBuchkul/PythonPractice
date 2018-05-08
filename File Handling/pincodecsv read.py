import csv
n=0

with open("p.csv",newline='')as csvfile:
      spamreader=csv.reader(csvfile,delimiter=',',quotechar='|')
      for row in spamreader:
            print(row[:2])
            for i in row:
                  l=i.split(',')[:2]
                  print(l)
                 # for j in i.split(','):
                  #      print()
            #print(','.join[:5])
            #break
'''
with open("pincode.csv",newline='')as csvfile:
      spamreader=csv.reader(csvfile,delimiter=',',quotechar='|')
      csv_writer=csv.writer(open("pin_scrap.csv",'w'))
      for row in spamreader:
            print(row[:2])
            for i in row:
                  l=i.split()[:2]
                  
'''
                  
                  
                  
                  

