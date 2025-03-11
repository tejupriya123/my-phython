def describe_pet(name, **attributes):
    print(f"Pet Name: {name}")
    for key, value in attributes.items():
        print(f"{key.capitalize()}: {value}")
