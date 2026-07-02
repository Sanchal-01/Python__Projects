# Making the Calculator

while True:
    try:

        a = int(input("Enter the first number: "))
        b = int(input("Enter the second number: "))

        print("Choose an Operation to perform.\n Press + for addition\n Press - for substraction\n Press * for multiplication\n Press / for division\n")

        Operation = input("Operation: ")
        
        match Operation:
            case '+':
                print(f"The result is {a + b}")
            case '-':
                print(f"The result is {a - b}")
            case '*':
                print(f"The result is {a * b}")
            case '/':
                print(f"The result is {a / b}")
            case default:
                print("Please select a valid Operation to perform.")


        # Ask the user if they want to play or exit first
        choice = input("Press 'q' to quit, or any other key to continue: ").strip().lower()
        if (choice == 'q' or 'quit'):
            print("Exiting the program. Goodbye!")
            break


    except Exception as e:
        print("Enter the valid value of a & b : ", e)

