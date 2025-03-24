from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

# Create all the instances for our classes 
menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()

# create a while loop 
is_on = True


while is_on:
    options = menu.get_items()
    choice = input(f"What would you like to drink? {options}: ").lower()
    # turn off or show report 
    if choice == "off":
        is_on = False
    elif choice == "report":
        coffee_maker.report()
        money_machine.report()
    else:
        # find the drink
        drink = menu.find_drink(choice) 
        if drink:
            # check if there is enough resources to make a drink
            if coffee_maker.is_resource_sufficient(drink):
            # process the payment
                print(f"Your total is: {drink.cost}")
                if money_machine.make_payment(drink.cost):
                    coffee_maker.make_coffee(drink)
