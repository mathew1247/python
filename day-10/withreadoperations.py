with open ("day-10/file.txt", "r") as file:
   print(file.read()) ## read the entire file
   file.seek(0) ## move the cursor to the beginning
   print(file.readline()) ## read the first line of the file



##--------------------------------------------------------#####
   with open ("day-10/file.txt", "r") as file:
       lines = file.readlines() ## read all lines into a list
##--------------------------------------------------------#####
   with open("day-10/file.txt", "r") as file:
       for line in lines:
           print(line.strip()) ## print each line without extra newlines


##--------------------------------------------------------#####
           with open ("day-10/file.txt","r") as file :
               print(file.readline())
           with open ("day-10/file.txt","r") as file :
               print(file.readlines())

##--------------------------------------------------------#####
with open("day-10/file.txt", "r") as file:
    print(file.tell())
    print(file.readlines())
    print(file.seek(4))
    print(file.tell())