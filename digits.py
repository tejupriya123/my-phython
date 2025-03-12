def sum_of_digits(number):
    
    number_str = str(abs(number))  
    total = 0
    
    for digit in number_str:
        total += int(digit)  
    
    return total
num = 12345
result = sum_of_digits(num)
