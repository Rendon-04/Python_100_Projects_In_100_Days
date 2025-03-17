MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

QUARTER_VALUE = 0.25
DIME_VALUE = 0.10
NICKEL_VALUE = 0.05
PENNY_VALUE = 0.01


def pay_for_coffee():
    """Processes coin input and returns the total amount inserted."""
    quarters = int(input("Enter number of quarters: "))
    dimes = int(input("Enter number of dimes: "))
    nickels = int(input("Enter number of nickels: "))
    pennies = int(input("Enter number of pennies: "))
    charge = (quarters * QUARTER_VALUE) + (dimes * DIME_VALUE) + (nickels * NICKEL_VALUE) + (pennies * PENNY_VALUE)
    return charge


def check_resources(drink):
    """Check if there are enough resources to make a drink and deduct resources if the drink is made."""
    needed = MENU[drink]["ingredients"]

    for item in needed:
        if resources[item] < needed[item]:
            print(f"Not enough {item} to make {drink}.")
            return False

    # Deduct resources
    for item in needed:
        resources[item] -= needed[item]

    return True


def drink_cost(drink):
    """Returns the cost of the selected drink."""
    return MENU[drink]["cost"]


def coffee_choice(drink_choice):
    """Handles drink selection, payment, and dispensing the coffee."""
    # Check if resources are available
    if check_resources(drink_choice):
        print(f"{drink_choice} is available.")
    else:
        print("Not enough resources to make that drink.")
        return  # Exit if not enough resources

    # Calculate and display the total cost
    total_amount = drink_cost(drink_choice)
    print(f'Please pay ${total_amount:.2f}')

    # Process payment
    print("Insert coins:")
    amount_paid = pay_for_coffee()

    while amount_paid < total_amount:
        amount_remaining = total_amount - amount_paid
        print(f"You paid ${amount_paid:.2f}, but the total is ${total_amount:.2f}. Please pay ${amount_remaining:.2f}.")
        additional_payment = pay_for_coffee()
        amount_paid += additional_payment
    if amount_paid > total_amount:
        change = amount_paid - total_amount
        print(f"Here is your change {change}")
    print(f"Here is your {drink_choice}! Enjoy 😊")


buying_coffee = True

while buying_coffee:
    coffee_selection = input("\nWhat would you like? (espresso, latte, cappuccino, report, off): ").lower()

    if coffee_selection in ["espresso", "latte", "cappuccino"]:
        coffee_choice(coffee_selection)

    elif coffee_selection == "report":
        print(f"Current resources: {resources}")

    elif coffee_selection == "off":
        print("Turning off the machine. Goodbye!")
        buying_coffee = False  

    else:
        print("Sorry, that option is not available. Please choose again.")
