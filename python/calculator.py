operator = input("What do you want to do? (+ - * /): ")
num1 = float(input("Enter a number: "))
num2 = float(input("And another number: "))

if operator == "+":
    result = num1 + num2
    print("The result is", round(result, 3))
elif operator == "-":
    result = num1 - num2
    print("The result is", round(result, 3))
elif operator == "*":
    result = num1 * num2
    print("The result is", round(result, 3))
elif operator == "/":
    result = num1 / num2
    print("The result is", round(result, 3))

else:
    print(f"{operator} is not valid. Please, enter a number")
