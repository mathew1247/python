import csv
with open("day-10/data.csv", "w", newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["Name", "Age", "City"])

##-----------------------------------##
import csv
with open("day-10/data.csv", "a", newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["Alice", 30, "New York"])
    writer.writerow(["Bob", 25, "Los Angeles"])

##-----------------------------------##
import csv
with open("day-10/data.csv", "w", newline=''  ) as file:
    writer = csv.writer(file)
    writer.writerow(["Name", "Age", "City"])

##-----------------------------------## 

           
