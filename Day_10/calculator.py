from calculator_art import logo
def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}

print(logo)
print("Welcome to your handy dandy calculator")

def calculator():
    should_accumulate =  True

    n1 = float(input("What is your first number?: "))
    while should_accumulate:

        for symbol in operations:
            print(symbol)
        operations_symbol = input("Pick an operations: ")
        n2 = float(input("What is the next number?: "))
        answer = operations[operations_symbol](n1, n2)
        print(f"{n1} {operations_symbol} {n2} = {answer}")



        choice = input(f"Type y to continue calculating with the {answer} from the previous step or type n")
        if choice == "y":
            n1 = answer
        else:
            should_accumulate = False
            print("\n"*20)
            calculator()
calculator()