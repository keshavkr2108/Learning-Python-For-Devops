def perform_operation():
    num1 = float(input("Enter the first number:"))
    num2 = float(input("Enter the second number:"))
    operation = int(input("Press 1 for Addition-\nPress 2 for Difference-\nPress 3 for Multiplication-\nPress 4 for Division-\nPress 5 for all-\nInput Operation:"))
    sum = int(num1 + num2)
    diff = int(abs(num1 - num2))
    mul = int(num1 * num2)
    div = float((num1 / num2))
    if operation == 1:
        print(f"Sum of given number is:{sum}")
    elif operation == 2:
        print(f"Difference if given number is:{diff}")
    elif operation == 3:
        print(f"Product of given number is:{mul}")
    elif operation == 4:
        print(f"Division value:{div}")
    elif operation == 5:
        print(f"Sum:{sum}, Difference:{diff}, Product:{mul}, Division:{div}")
    else:
        print("Invalid Operation")
perform_operation()        
