num1 = int(input("enter first number: "))
num2 = int(input("enter second number: "))
num3 = int(input("enter third number: "))

operation = input("please enter(Please enter (+, -, * or /): ")

if operation == "+":
    print(num1 + num2 + num3)
elif operation == "-":
    print(num1 - num2 - num3)
elif operation == "*":
    print(num1 * num2 * num3)
elif operation == "/":
    print(num1 / num2 / num3)