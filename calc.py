# Building a simple calculator
# This calculator should allow the person to enter any 2 numbers and a matematical operation
# Perform the operation based on the user's input and print the result.
# Ask the user for two numbers and the mathematical operation1

# Display a menu of mathematical operations for the user to choose from

print("Select an operation to perfom:")
print("1. ADDITION")
print("2. SUBTRACTION")
print("3. MULTIPLICATION")
print("4. DIVISION")

# Allow the user to enter any two numbers of choice and an operation

operation = input()

if operation == "1":
    num1 = input("Enter the first number: ")
    num2 = input("Enter the second number: ")
    print("The answer is " + str(int(num1) + int(num2)))
elif operation == "2":
    num1 = input("Enter the first number: ")
    num2 = input("Enter the second number: ")
    print("The answer is " + str(int(num1) - int(num2)))
elif operation == "3":
    num1 = input("Enter the first number: ")
    num2 = input("Enter the second number: ")
    print("The answer is " + str(int(num1) * int(num2)))
elif operation == "4":
    num1 = input("Enter the first number: ")
    num2 = input("Enter the second number: ")
    print("The answer is " + str(int(num1) / int(num2)))
else:
    print("Entry is invalid")
