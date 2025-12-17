

print("Simple Calculator")

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

print("Select Operation: +  -  *  /")
op = input("Enter operation: ")

if op == '+':
    print("Result:", num1 + num2)
elif op == '-':
    print("Result:", num1 - num2)
elif op == '*':
    print("Result:", num1 * num2)
elif op == '/':
    if num2 == 0:
        print("Error: Division by zero not allowed!")
    else:
        print("Result:", num1 / num2)
else:
    print("Invalid Operation")
