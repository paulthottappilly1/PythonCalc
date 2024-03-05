from art import logo

#function to add two numbers up
def add(num1, num2):
    return num1 + num2

#function to subtract the first number with the second number
def subtract(num1, num2):
    return num1 - num2

#function to multiply both numbers up
def multiply(num1, num2):
    return num1 * num2

#function to divide the first number with the second number
def divide(num1, num2):
    return num1 / num2

#dictionary that holds the operations for the calculator 
operations = {
    "+": add,
    "-": subtract, 
    "*": multiply, 
    "/": divide
    }

#created a function for the calculator
def calculator():
    print(logo)
#created a variable to exit the while loop
    calculation_finished = False
    #prompting the user to input the first number
    num1 = float(input("What's the first number?: "))

    #while loop that'll keep running until the user wants to exit the program 
    while not calculation_finished:
        for symbol in operations:
            print(symbol)
        operation_symbol = input("Please select an operation above for the calculation: ")
        num2 = float(input("What's the next number?: "))
        operation = operations[operation_symbol]
        answer = operation(num1, num2)

        print(f"{num1} {operation_symbol} {num2} = {answer}")

        #prompts the user to decide if they want to keep working with the answer, exit the program, or restart the calculator for a completely new set of numbers
        is_calculation_finished = input(f"Type 'y' to continue calculating with {answer}, type 'n' to exit, or type 'r' to restart the calculator: ")
        if  is_calculation_finished == 'n':
            calculation_finished = True
            print("Goodbye, have a wonderful day!")
            exit()
        elif is_calculation_finished == 'y':
            num1 = answer
        elif is_calculation_finished == 'r':
            calculator()

calculator()