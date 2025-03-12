def sum_of_digits(number):
    
    number = abs(number)
    
    
    total = sum(int(digit) for digit in str(number))
    
    return total


num = 12345
result = sum_of_digits(num)

print(f"The sum of digits of {num} is: {result}")
