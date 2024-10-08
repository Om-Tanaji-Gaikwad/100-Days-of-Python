# Calculator using Dictionary and Function input/output
def add(n1,n2):
    return n1 + n2
def substract(n1,n2):
    return n1 - n2
def multiply(n1,n2):
    return n1 * n2
def divide(n1,n2):
    return n1 / n2
a=int(input("Enter value of number 1:\n"))
c=input("Enter operation you want to perform(+,-,*,/) :\n")
b=int(input("Enter value of number 2:\n"))
calculator={
    "+":add,
    "-":substract,
    "*":multiply,
    "/":divide
}
result=calculator[c](a,b)
print(f"{a} {c} {b} = {result}")
while(True):
    ask= input(f"Do you want to continue with value {result} ?(y-yes,n-no)\n").lower()
    if ask=="y":
        a=result
        c = input("Enter operation you want to perform(+,-,*,/) :\n")
        b = int(input("Enter value of number 2:\n"))
        result=calculator[c](a,b)
    elif ask=="n":
        a=int(input("Enter value of number 1:\n"))
        c = input("Enter operation you want to perform(+,-,*,/) :\n")
        b = int(input("Enter value of number 2:\n"))
        result = calculator[c](a, b)
    else:
        print("Invalid Input!")
    result = calculator[c](a, b)
    print(f"{a} {c} {b} = {result}")
