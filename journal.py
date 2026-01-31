#Creating a file
file = open("example.txt",'w')

#Write onto the file
file.write("Hello, World!\n")
file.write("Hello, Sourish!\n")
file.write("Happy New Year!\n")
file.close()

#Open a file and read only mode
file = open("example.txt","r")
content = file.read()
print("file content:\n" + content)

#Close the file
file.close()

print("-"*50)

#Reading a file line by line
file = open("example.txt","r")
print(file.readline())
print(file.readline())
file.close()

print("-"*50)

#Appending to a file
file = open("example.txt","a")
file.write("I like python\n")
file.close()

file = open("example.txt","r")
content = file.read()
print("file content:\n" + content)
file.close()

#Writing the file using with 
"""With statement used to automatically close the file."""
with open("data.txt","w") as file:
    file.write("Line 1\n")

#Appending to a file using with
with open("data.txt","a")as file:
    file.write("Line 2\n")

#Reading a file usng with
with open("data.txt","r")as file:
    print(file.read())
