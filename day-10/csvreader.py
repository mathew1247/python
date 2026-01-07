import csv
with open("day-10/data.csv", "r", newline="") as file:
    reader = csv.reader(file)
    print(file.read()) 

##-----------------------------------##
with open("day-10/data.csv", "r", newline="") as file:
    reader = csv.reader(file)
    print(file.read()) ## for read the file content
    for row in reader:
        print(row) ## for read the file content in a list format