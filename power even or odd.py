def power_even_or_odd(base, exponent):
    
    result = base ** exponent
    
    
    if result % 2 == 0:
        return f"{base}^{exponent} = {result}, which is even."
    else:
        return f"{base}^{exponent} = {result}, which is odd."


print(power_even_or_odd(2, 3))
print(power_even_or_odd(3, 3))
