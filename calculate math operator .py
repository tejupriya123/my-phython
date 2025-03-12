import math

def calculate_math_operations(number):
    
    square_root = math.sqrt(number)
    
    
    factorial = math.factorial(number) if number >= 0 and isinstance(number, int) else "undefined"
    
    
    sine_value = math.sin(math.radians(number))

    
    print(f"Square root of {number}: {square_root}")
    print(f"Factorial of {number}: {factorial}")
    print(f"Sine of {number} degrees: {sine_value}")


num = 5
calculate_math_operations(num)
