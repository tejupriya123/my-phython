def access_dictionary():
    print("teju-070")
    sample_dict = {
        "name": "Alice",
        "age": 25,
        "city": "New York",
        "profession": "Engineer"
    }

    
    key = input("Enter the key you want to access: ")

    
    value = sample_dict.get(key)

    
    if value is not None:
        print(f"The value for key '{key}' is: {value}")
    else:
        print(f"Key '{key}' not found in the dictionary.")



access_dictionary()
