def unpack_tuple(my_tuple):
    
    a, b, c = my_tuple
    
    print(f"Value of a: {a}")
    print(f"Value of b: {b}")
    print(f"Value of c: {c}")

tuple_example = (10, 20, 30)
unpack_tuple(tuple_example)
def dynamic_unpack(my_tuple):
    for index, value in enumerate(my_tuple):
        print(f"Value {index + 1}: {value}")


dynamic_unpack((1, 2, 3, 4, 5))
