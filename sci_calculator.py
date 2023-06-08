import math

# Store the current result and number of calculations
current_result = 0.0
num_calculations = 0
total = 0

    # Display menu

calculator_menu =   (f"Calculator Menu\n"
                    "---------------\n"
                    "0. Exit Program\n"
                    "1. Addition\n"
                    "2. Subtraction\n"
                    "3. Multiplication\n"
                    "4. Division\n"
                    "5. Exponentiation\n"
                    "6. Logarithm\n"
                    "7. Display Average\n")

print(f"Current Result: {current_result}\n\n")
print(calculator_menu)


# Main calculator loop
while True:
    menu_choice = int(input("\nEnter Menu Selection: "))

    # Exit program
    if menu_choice == 0:
        print('Thanks for using this calculator. Goodbye!')
        break
    
    
    # Read operands and perform calculation    
    elif menu_choice in [1, 2, 3, 4, 5, 6]:

    # Read operands
        # Read first operand
        first_operand = input("Enter first operand: ")
        if first_operand == "RESULT":
            first_operand = current_result
        else:
            first_operand = float(first_operand)

        # Read second operand
        second_operand = input("Enter second operand: ")
        if second_operand == "RESULT":
            second_operand = current_result
        else:
            second_operand = float(second_operand)

    # Performing the calculation
        if menu_choice == 1:
            current_result = first_operand + second_operand
            num_calculations += 1
            total += current_result

        elif menu_choice == 2:
            current_result = first_operand - second_operand
            num_calculations += 1
            total += current_result

        elif menu_choice == 3:
            current_result = first_operand * second_operand
            num_calculations += 1
            total += current_result

        elif menu_choice == 4:
            current_result = first_operand / second_operand
            num_calculations += 1
            total += current_result

        elif menu_choice == 5:
            current_result = first_operand ** second_operand
            num_calculations += 1
            total += current_result

        elif menu_choice == 6:
            current_result = math.log(second_operand, first_operand)
            num_calculations += 1
            total += current_result
        print(f"Current Result: {current_result}\n\n")   
        print(calculator_menu)

    elif menu_choice == 7:          
        if num_calculations == 0:
            print("Error: No calculations yet to average!", end='\n',)
            continue

        else:
            average = total / num_calculations
        print("Sum of calculations:", total)
        print("Number of calculations:", num_calculations)
        print(f"Average of calculations: {average:.2f}\n\n")
        continue
                      
    else:
        print("Error: Invalid selection!")
        continue
