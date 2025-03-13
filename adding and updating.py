def manage_dictionary():
    my_dict = {}

    while True:
        print("\nDictionary Manager:")
        print("1. Add/Update Element")
        print("2. View Dictionary")
        print("3. Exit")
        
        choice = input("Enter your choice (1-3): ")

        if choice == '1':
            key = input("Enter the key: ")
            value = input("Enter the value: ")
            my_dict[key] = value
            print(f"Element added/updated: {key} -> {value}")

        elif choice == '2':
            print("\nCurrent Dictionary:")
            for k, v in my_dict.items():
                print(f"{k}: {v}")

        elif choice == '3':
            print("Exiting the program. Goodbye!")
            break

        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

manage_dictionary()
