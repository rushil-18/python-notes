blah = input("enter some u wanna add in file:")

file = open("file.txt" , "w")
file.write(blah)                  # creates a goddamn file and writes

#run it again youre gonna get your 1st input replaced 

file = open("file.txt" , "a")
file.write(f"blah\n")            #appends in file dosent replace shit like w 

file.close()

#better with 'with'

with open("file.txt" , "w") as file:
    file.write(f"{blah}\n")

with open("file.txt" , "r") as file:
    lines = file.readlines() #reads all lines
    line = file.readline() #reads a line 
    read = file.read() #


for line in lines:
    a =sorted((line.rstrip()))
    print(a)           #removes white spaces and sort them in alphabatical order
    
#with csv 

with open("file.csv", "r") as file:
    for line in file:
        row = line.rstrip().split(",")
        print(f"{row[0]} - row[1]")   #divides csv lines like table values 

