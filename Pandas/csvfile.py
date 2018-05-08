import csv
with open('nyc.csv', 'rb') as csvfile:
      spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
      for row in spamreader:
            print(', '.join(row))
