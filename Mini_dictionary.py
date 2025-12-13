dictionary = {}
while True:
    print(f'\n my dictionary app\n')
    print("1. Add/update a word")
    print("2. Retrieve a word's definition")
    print("3. Delete a word")
    print("4. View all words")
    print("5. Exit")
    
    choice = int(input("\n Pick an option from 1-5: "))
    if choice == 1:
        word = input("\n Enter a word: ").strip()
        definition = input("\n Enter the definition: ").strip()
        dictionary[word] = definition
        print(f"\n Word '{word}' added successfully")

    elif choice == 2:
        word = input("\n Enter the word to retrieve the definition: ")
        if word in dictionary:
            print(f"\n {word}: {dictionary[word]}")
        else: 
            print(f"\n The Word {word} is not in the dictionary")
    
    elif choice == 3:
        word = input("\n Pick a word to delete: ")
        if word in dictionary:
            del dictionary[word]
            print(f"\n The Word {word} has been deleted")
        else:
            print(f"\n The Word {word} is not in the dictionary")

    elif choice == 4:
        if dictionary:
            print(f"\n Words in the dictionary are: ")
            for word in dictionary:
                print(f"{word}: {dictionary[word]} ")
        else:
            print("\n There are no more words in the dictionary")
    
    elif choice == 5:
        print("\n Thanks for using the mini dictionary app, Goodbye!")
        break
    
    else:
        print("\n You can only choose from 1-5")
