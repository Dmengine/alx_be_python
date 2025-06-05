num1 = float(input("Enter the first number: "))  # Must match this prompt exactly
num2 = float(input("Enter the second number: "))  # Must match this prompt exactly
operation = input("Choose the operation (+, -, *, /): ")  # Must match this prompt exactly

match operation:  # Use the match-case structure introduced in Python 3.10+
    case "+":
        result = num1 + num2
        print(f"The result is {result}")  # Must start with "The result is"
    case "-":
        result = num1 - num2
        print(f"The result is {result}")
    case "*":
        result = num1 * num2
        print(f"The result is {result}")
    case "/":
        if num2 == 0:
            print("Cannot divide by zero.")  # Must match this wording exactly
        else:
            result = num1 / num2
            print(f"The result is {result}")
    case _:
        print("Invalid operation.")