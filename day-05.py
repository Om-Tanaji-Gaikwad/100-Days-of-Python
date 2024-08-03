# Password Generator
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
print("Welcome to the PyPassword Generator!")
l= int(input("How many letters would you like in your password?\n"))
s= int(input(f"How many symbols would you like?\n"))
n= int(input(f"How many numbers would you like?\n"))
# Easy Password
"""
let=""
sym=""
num=""
for a in range (0,l):
    le = random.randint(0, len(letters) - 1)
    let=let+letters[le]
for a in range (0,s):
    sy = random.randint(0, len(symbols) - 1)
    sym=sym+symbols[sy]
for a in range (0,n):
    nu = random.randint(0, len(numbers) - 1)
    num=num+numbers[nu]
password=let+sym+num
print(password)
"""
# Hard Password
let=""
sym=""
num=""
for a in range (0,l):
    le = random.randint(0, len(letters) - 1)
    let=let+letters[le]
for a in range (0,s):
    sy = random.randint(0, len(symbols) - 1)
    sym=sym+symbols[sy]
for a in range (0,n):
    nu = random.randint(0, len(numbers) - 1)
    num=num+numbers[nu]
password=let+sym+num
password_list=[]
for a in range (0,len(password)):
    password_list += password[a]
random.shuffle(password_list)
password1=""
for a in range (0,len(password_list)):
    password1 += password_list[a]
print(f"Your Generated Password : {password1}")