# Faulty calculator
operator = input("Enter operator:")
var1 = int(input("Enter first number="))
var2 = int(input("Enter second number="))
if operator == "+":
    if var1 == 56 and var2 == 9:
        print("77")
    else:
        print("Sum is :", var1+var2)

if operator == "*":
    if var1 == 45 and var2 == 3:
        print("Product is:555")
    else:
        print("Product is :", var1*var2)
if operator == "/":
    if var1 == 56 and var2 == 3:
        print("The quotient is:4")
    else:
        print("The quotient is:", float(var1/var2))

if operator == "-":
    print("The Substraction of numbers is:", var1-var2)