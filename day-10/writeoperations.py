##-----------------------------------##
file = open("day-10/file.txt", "a")
file.write("Hello, World!\n")
file.write("say my name\n")
file.close()

##without the append mode it will not override the content in the file 
##by using the write mode will erase the previous content and stored the new txt

##------------------------------------##
with open ("day-10/file.txt", "a") as file:#->the file the name to be used as an object 
  file.write("hii heisenberg\n")


##------------------------------------##

file = open("day-10/file.txt", "a")
file.writelines(["high\n", "say my name\n"])
file.close()

##------------------------------------##