while True:
    print("****Arithmetic Calculator****")
    print("Enter 1 for Addition(+)")
    print("Enter 2 for Subtraction(-)")
    print("Enter 3 for Multiply(*)")
    print("Enter 4 for Division(/)")
    print("Enter 5 for Modulus(%)")
    print("Enter 6 to exit the program")
    c = int(input("Enter your choice: "))
    if c == 1:
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))
        print("Addition is: ", a + b)
    elif c == 2:
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))
        print("Subtraction is: ", a - b)
    elif c == 3:
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))
        print("Multiplication is: ", a * b)
    elif c == 4:
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))
        if b == 0:
            print("Division by zero error")
        else:
            print("Division is: ", a / b)

    elif c == 5:
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))
        if b == 0:
            print("Division by zero error!!!!")
        else:
            print("Remainder is: ", a % b)

    elif c == 6:
        break #used to terminate the program once the condition is met
    else:
        print("Invalid Input!!!")
