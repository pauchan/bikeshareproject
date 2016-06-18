import csv

with open("data/original/train.csv") as csvfile:
  reader = csv.reader(csvfile, delimiter=',', quotechar='|')
  for row in reader:
    print ', '.join(row)
