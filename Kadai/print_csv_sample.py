import csv

csv_file = open("./temp_only_sample1.csv", "r", encoding = "utf-8", errors = "", newline = "")

f = csv.reader(csv_file, delimiter = ",", doublequote = True, lineterminator = "\r\n", quotechar = '"', skipinitialspace = True)

header = next(f)

print(header)

for row in f:
    print(row)