def calculator(num1, num2, operator):
    if operator == '+':
        return num1 + num2
    elif operator == '-':
        return num1 - num2
    elif operator == '*':
        return num1 * num2
    elif operator == '/':
        if num2 != 0:
            return num1 / num2
        else:
            return "Error: Division by zero is not allowed."
    elif operator == '%':
        return num1 % num2
    elif operator == '**':
        return num1 ** num2
    else:
        return "Error: Invalid operator."


result = calculator(10, 5, '+')
print(f"Result: {result}")
