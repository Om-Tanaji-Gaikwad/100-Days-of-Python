# Coffee Machine
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
money = 0
def report(money):
    print(f"Water={resources["water"]}ml\nMilk={resources["milk"]}ml\nCoffee={resources["coffee"]}g\nMoney=RS.{money}")

def coins():
    a=float(input("Enter number of quarters :\n"))*0.25
    b=float(input("Enter number of dimes :\n"))*0.10
    c= float(input("Enter number of nickles :\n")) * 0.05
    d= float(input("Enter number of pennies :\n")) * 0.01
    total=a+b+c+d
    return round(total,2)
def transaction(total,money):
    if money == total:
        print("Transaction Successful.")
        return True
    elif money>total:
        print("Insufficient money!")
        return False
    elif money<total:
        change=total-money
        print(f"Here is your change ${change}")
        return True
def espresso():
    if resources["water"]>=MENU["espresso"]["ingredients"]["water"] and resources["coffee"]>=MENU["espresso"]["ingredients"]["coffee"]:
        money=0
        money += MENU["espresso"]["cost"]
        print(f"Your cost is $ {money}")
        total=coins()
        is_paid=transaction(total,money)
        if is_paid==True:
            resources["water"] -= MENU["espresso"]["ingredients"]["water"]
            resources["coffee"] -= MENU["espresso"]["ingredients"]["coffee"]
            print("Here is your espresso . Enjoy!")
            return money
        else:
            print("Your money is returned to you.")
            return 0
    elif resources["water"]<MENU["espresso"]["ingredients"]["water"]:
        print("Insufficient Water")
        return 0
    elif resources["coffee"]<MENU["espresso"]["ingredients"]["coffee"]:
        print("Insufficient Coffee")
        return 0


def latte():
    if resources["water"]>=MENU["latte"]["ingredients"]["water"] and resources["coffee"]>=MENU["latte"]["ingredients"]["coffee"] and resources["milk"]>=MENU["latte"]["ingredients"]["milk"]:
        money=0
        money += MENU["latte"]["cost"]
        print(f"Your cost is $ {money}")
        total = coins()
        is_paid = transaction(total, money)
        if is_paid == True:
            resources["water"] -= MENU["latte"]["ingredients"]["water"]
            resources["coffee"] -= MENU["latte"]["ingredients"]["coffee"]
            resources["milk"] -= MENU["latte"]["ingredients"]["milk"]
            print("Here is your latte . Enjoy!")
            return money
        else:
            print("Your money is returned to you.")
            return 0
    elif resources["water"]<MENU["latte"]["ingredients"]["water"]:
        print("Insufficient Water")
        return 0
    elif resources["milk"]<MENU["latte"]["ingredients"]["milk"]:
        print("Insufficient Milk")
        return 0
    elif resources["coffee"]<MENU["latte"]["ingredients"]["coffee"]:
        print("Insufficient Coffee")
        return 0
def cappuccino():
    if resources["water"]>=MENU["cappuccino"]["ingredients"]["water"] and resources["coffee"]>=MENU["cappuccino"]["ingredients"]["coffee"] and resources["milk"]>=MENU["cappuccino"]["ingredients"]["milk"]:
        money=0
        money += MENU["cappuccino"]["cost"]
        print(f"Your cost is $ {money}")
        total = coins()
        is_paid = transaction(total, money)
        if is_paid == True:
            resources["water"] -= MENU["cappuccino"]["ingredients"]["water"]
            resources["coffee"] -= MENU["cappuccino"]["ingredients"]["coffee"]
            resources["milk"] -= MENU["cappuccino"]["ingredients"]["milk"]
            print("Here is your Cappuccino . Enjoy!")
            return money
        else:
            print("Your money is returned to you.")
            return 0
    elif resources["water"]<MENU["cappuccino"]["ingredients"]["water"]:
        print("Insufficient Water")
        return 0
    elif resources["milk"]<MENU["cappuccino"]["ingredients"]["milk"]:
        print("Insufficient Milk")
        return 0
    elif resources["coffee"]<MENU["cappuccino"]["ingredients"]["coffee"]:
        print("Insufficient Coffee")
        return 0
is_on=True
while is_on==True:
    choice = input("What would you like ? (espresso/latte/cappuccino):\n").lower()
    if choice == "report":
        report(money)
    elif choice == "off":
        print("Turning off the coffee machine...")
        break
    elif choice == "espresso":
        money+=espresso()
    elif choice == "latte":
        money+=latte()
    elif choice == "cappuccino":
        money+=cappuccino()
    else:
        print("Invalid Input!")
