number1 = float(input("Enter first number:"))
number2 = float(input("Enter second number:"))
myoperator= str(input("Select operator(+,-,*,/): "))

add = number1 + number2
difference: object = number1 - number2
multiply = number1 * number2
divide = number1 / number2


if myoperator == "+":
    print("The sum of the two numbers is ", add)
elif myoperator == "-":
    print("The difference between the two numbers is ", difference)
elif myoperator == "*":
    print("The product of the two numbers is ", multiply)
elif myoperator=="/":
    print("The quotient of the two numbers is ", divide)
