def add(x,y):
    return x + y

def subtract(x,y):
    return x-y

def multiply(x,y):
    return x * y

def divide(x,y):
    return x / y

print("Select Operation")
print("1.Add")
print("2.Subract")
print("3.Multiply")
print("4.Divide")

while  True:
    choice = input("Enter 1/2/3/4 to select the operation: ")
    if choice in('1', '2', '3', '4'):
        num1 = float(input("Enter your first number: "))
        num2 = float(input("Enter your second number: "))

        if choice == '1':
            print(num1, "+", num2, "=", add(num1, num2))

        elif choice == '2':
            print(num1, "-", num2, "=", subtract(num1, num2))

        elif choice == '3':
            print(num1, "*", num2, "=", multiply(num1, num2))

        elif choice == '4':
            print(num1, "/", num2, "=", divide(num1, num2))

        new_calculation = input("Would you like to do another calculation? (yes/no): ")
        if new_calculation == "no":
            print("Shutting down")
            break
    else:
        print("Invalid Input")