print("***Simple Calculator***")

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

print("Choose an operation")
print("+ for Addition")
print("- for Subtraction")
print("* for Multiplication")
print("/ for Division")

operation = input("Enter operation: ")

if operation == "+":
    result = num1 + num2
    print("Result =", result)

elif operation == "-":
    result = num1 - num2
    print("Result =", result)

elif operation == "*":
    result = num1 * num2
    print("Result =", result)   

elif operation == "/":
    if num2 != 0:
        result = num1 / num2
        print("Result =", result)
    else:
        print("Cannot divide by zero")

else:
    print("Invalid choice")
