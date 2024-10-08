# Tip Calculator
print("Welcome to the tip calculator !")
a=float(input("What was the total bill ? \n Rs."))
b=float(input("How much tip you wanna give ? \n Rs."))
c=int(input("How many people to split the bill ? \n "))
bill= (a+b)/c
print(f"Each person should pay : Rs.{bill}")