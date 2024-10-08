# OOP

# from turtle import Turtle, Screen
# kasav= Turtle()
# print(kasav)
# kasav.shape("turtle")
# kasav.color("green")
# kasav.forward(100)
# my_screen=Screen()
# print(my_screen.canvheight)
# my_screen.exitonclick()

from day_16_menu import Menu
from day_16_coffee_maker import CoffeeMaker
from day_16_money_machine import MoneyMachine

money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()
menu = Menu()

is_on = True

while is_on:
    options = menu.get_items()
    choice = input(f"What would you like? ({options}): ")
    if choice == "off":
        is_on = False
    elif choice == "report":
        coffee_maker.report()
        money_machine.report()
    else:
        drink = menu.find_drink(choice)

        if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
            coffee_maker.make_coffee(drink)
