def cups_to_grams(cups, ingredient):
    conversion_rates = { "flour": 120,  # 1 cup = 120g sugar
                        "sugar": 200,
                        "butter": 250}
    if ingredient in conversion_rates:
        grams = cups * conversion_rates[ingredient]
        return grams
    else:
        return "ingredient is not available"
    
#Converting tablespoons into teaspoons
def tablespoons_to_teaspoons(tablespoons):
    return tablespoons * 3 # 1tbsp = 3tsp

def grams_to_cups(grams, ingredient):
    conversion_rates = { "flour": 120,  
                        "sugar": 200,
                        "butter": 250}
    if ingredient in conversion_rates:
        cups = grams / conversion_rates[ingredient] 
        return cups
    else:
        return "ingredient is not available"
    
def recipe_converter():
    while True:
        print("\n Recipe Converter App")
        print("1. Convert cups to grams")
        print("2. Convert tablespoons to teaspoons")
        print("3. Convert grams to cups")
        print("4. Exit")

        choice = int(input("Pick an option from 1 to 4: "))
        if choice == 1:
            cups = float(input("Enter the number of cups: "))
            ingredient = input("Enter the ingredient (flour, sugar, butter): ").strip().lower()
            result = cups_to_grams(cups, ingredient)
            print(f"Result:{result} grams")
        
        elif choice == 2:
            tablespoons = float(input("Enter the number of tablespoons: "))
            result = tablespoons_to_teaspoons(tablespoons)
            print(f"Result:{result} teaspoons")
        
        elif choice == 3:
            grams = float(input("Enter the number of grams: "))
            ingredient = input("Enter the ingredient (flour, sugar, butter): ").strip().lower()
            result = grams_to_cups(grams, ingredient)
            print(f"Result:{result} cups")
        
        elif choice == 4:
            print("Thanks for using the recipe converter app, Bye!")
            break
        else:
            print("Invalid choice, Try again")
            
recipe_converter()
