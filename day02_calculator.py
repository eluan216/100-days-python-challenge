def calculator():
    print("===== SMART CALCULATOR =====")

Num1 = float(input("Enter first number: "))
operator = input("Enter operator (+, -, *, /): ")
Num2 = float(input("Enter second number: "))

if operator == "+":
    result = Num1 + Num2
    print(f"{Num1} + {Num2} = {result}")
elif operator == "-":
    result = Num1 - Num2
    print(f"{Num1} - {Num2} = {result}")
elif operator == "*":
    result = Num1 * Num2
    print(f"{Num1} * {Num2} = {result}")
elif operator == "/":
    if Num2 != 0:
        result = Num1 / Num2
        print(f"{Num1} / {Num2} = {result}")
    else:
        print("Error: Division by zero is not allowed.")

        
calculator()