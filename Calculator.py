def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y != 0:
        return x / y
    else:
        return "Error: Division by zero"

# Get user input
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# Display operation choices
print("Select operation:")
print("1. Addition (+)")
print("2. Subtraction (-)")
print("3. Multiplication (*)")
print("4. Division (/)")

# Get user operation choice
choice = input("Enter choice (1/2/3/4): ")

# Perform calculation based on user choice
if choice == '1':
    result = add(num1, num2)
    operator = "+"
elif choice == '2':
    result = subtract(num1, num2)
    operator = "-"
elif choice == '3':
    result = multiply(num1, num2)
    operator = "*"
elif choice == '4':
    result = divide(num1, num2)
    operator = "/"
else:
    result = "Error: Invalid Input"
    operator = ""

# Display the result
print(f"{num1} {operator} {num2} = {result}")
