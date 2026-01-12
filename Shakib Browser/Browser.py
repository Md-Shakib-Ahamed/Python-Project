import math

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Cannot divide by zero"
    else:
        return x / y

def square_root(x):
    if x < 0:
        return "Cannot find square root of negative number"
    else:
        return math.sqrt(x)

def logarithm(x, base=10):
    if x < 0:
        return "Cannot find logarithm of negative number"
    elif base <= 0 or base == 1:
        return "Invalid base"
    else:
        return math.log(x, base)

def sine(x):
    return math.sin(x)

def cosine(x):
    return math.cos(x)

def tangent(x):
    return math.tan(x)

def main():
    print("Welcome to SAM CAL")
    print("Please select an operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Square root")
    print("6. Logarithm")
    print("7. Sine")
    print("8. Cosine")
    print("9. Tangent")

    choice = input("Enter operation number (1-9): ")

    if choice in ['1', '2', '3', '4']:
        x = float(input("Enter first number: "))
        y = float(input("Enter second number: "))

        if choice == '1':
            print("Result: ", add(x, y))
        elif choice == '2':
            print("Result: ", subtract(x, y))
        elif choice == '3':
            print("Result: ", multiply(x, y))
        elif choice == '4':
            print("Result: ", divide(x, y))
    elif choice in ['5', '6']:
        x = float(input("Enter a number: "))

        if choice == '5':
            print("Result: ", square_root(x))
        elif choice == '6':
            base = float(input("Enter base: "))
            print("Result: ", logarithm(x, base))
    elif choice in ['7', '8', '9']:
        x = float(input("Enter angle in radians: "))

        if choice == '7':
            print("Result: ", sine(x))
        elif choice == '8':
            print("Result: ", cosine(x))
        elif choice == '9':
            print("Result: ", tangent(x))
    else:
        print("Invalid operation number")

if __name__ == '__main__':
    main()
