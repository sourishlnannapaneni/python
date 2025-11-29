my_dict = {"apple":"A red coloured fruit", "orange":"An orange coloured fruit", "Books":"Something you read"}
print(f'\n my dictionary = {my_dict}\n')
#Adding a new item into the dictionary
my_dict["pen"] = "Something you write with"
print(f'\n my dictionary = {my_dict}\n')
#Printing only keys for a dictionary
print(f'keys = {my_dict.keys()}\n')
#Printing only values for a dictionary
print(f'values = {my_dict.values()}\n')
#deleting an item from a dictionary
del my_dict["apple"]
print(my_dict)
#Removing an item from a dictionary
my_dict.pop("Books")
print(my_dict)
#Updatining an item from a dictionary
my_dict["orange"] = "A citrus fruit"
print(my_dict)
#To check if a key exists in our dictionary
n = input("Enter any key name: ")
if n in my_dict: 
    print("Key exists")
else:
    print("Key doesn't exist")
