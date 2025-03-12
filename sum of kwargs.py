def sum_of_kwargs(**kwargs):
    
    return sum(kwargs.values())


result = sum_of_kwargs(a=10, b=20, c=30)

print(f"The sum of the keyword arguments is: {result}")
