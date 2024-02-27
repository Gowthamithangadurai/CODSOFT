def add(x, y):
    return x + y

def subtraction(x, y):
    return x - y

def multiplication(x, y):
    return x * y

def divide(x, y):
    return x / y if y != 0 else "Cannot divide by zero"

print("Select your option: (1, 2, 3, 4)")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Divide")

option = int(input("Enter your option: "))
x = int(input("Enter number 1: "))
y = int(input("Enter number 2: "))

if option == 1:
    result = add(x, y)
    print("Result:", result)
elif option == 2:
    result = subtraction(x, y)
    print("Result:", result)
elif option == 3:
    result = multiplication(x, y)
    print("Result:", result)
elif option == 4:
    result = divide(x, y)
    print("Result:", result)
else:
    print("Invalid option")
