def safe_calculator():
    print("\n Welcome to the safe calculator!")
    while True:
        try:
            num1 = float(input("Enter the first number: "))
        except ValueError:
            print("Invalid input! Please enter a valid number.")
            continue
        
        try: 
            num2 = float(input("Enter the second number: "))
        except ValueError:
            print("Invalid input! Please enter a valid number.")
            continue

        operator = input("Enter operator (+, -, *, /)").strip()
        #Performing calculations
        try: 
            if operator == "+":
                result = num1 + num2
            
            elif operator == "-":
                result = num1 - num2

            elif operator == "*":
                result = num1 * num2

            elif operator == "/":
                result = num1 / num2

            else:
                raise ValueError("Invalid operator")
            
        except ZeroDivisionError:
            print("Error: Cannot divide by Zero!")
            continue

        except ValueError:
            print("Invalid operator! Please use +, -, * or /.")
            continue

        print("The result is: ", result)

        continue_calc = input("\n Do you want to perform another calculation? (yes/no):").strip().lower()
        if continue_calc != "yes":
            print("Thank you for using the Safe Calculator. Goodbye!")
            break

safe_calculator()
