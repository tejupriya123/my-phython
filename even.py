def check_even_or_odd(number):
    if number % 2 == 0:
        return f"{number} is even."
    else:
        return f"{number} is odd."


num = 7
result = check_even_or_odd(num)

print(result)
