import csv

outfile = open("data-ready.csv", 'w')

with open('data.csv', 'r') as f:
    reader = csv.reader(f, delimiter=",")
    
    for row in reader:
        animal = row[0]
        classification = row[1]
        line = "['{}', '{}'],\n".format(classification, animal)
        outfile.write(line)
outfile.close()