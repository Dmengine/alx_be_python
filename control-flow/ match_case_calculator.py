num1 = float(input("Enter the first number: "))  #Check: input prompt for first number
num2 = float(input("Enter the second number: "))  #Check: input prompt for second number
operation = input("Choose the operation (+, -, *, /): ")  #Check: prompt for operation

match operation:  #Check: match-case used
    case "+":
        result = num1 + num2
        print(f"The result is {result}")  #Output result message
    case "-":
        result = num1 - num2
        print(f"The result is {result}")
    case "*":
        result = num1 * num2
        print(f"The result is {result}")
    case "/":
        if num2 == 0:
            print("Cannot divide by zero.")  #Check: handles division by zero
        else:
            result = num1 / num2
            print(f"The result is {result}")
    case _:
        print("Invalid operation.")