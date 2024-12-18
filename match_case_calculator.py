#Prompt user to enter two numbers
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

#Enter operation
operation = input("Choose the operation (+, -, *, /): ")
#Calculate using match case

match operation:
    case "+":
        result = num1 + num2
        print(f"The result is {result}")
    case "-":
        result= num1 - num2
        print(f"The result is {result}")
    case "*":
        result = num1 * num2
        print(f"The result is {result}")
    case "/":
        if num2 != 0:
            result = num1 / num2
            print(f"The result is {result}")
        else:
            print("Errot: Division by zero is not allowed")
    case _:
        print("Invalid operation. Please choose one of (+, -, *, /)")
