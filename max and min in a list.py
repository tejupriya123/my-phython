def find_min_max(numbers):
    if not numbers:
        return None, None
    
    smallest = min(numbers)
    largest = max(numbers)
    
    return smallest, largest


numbers = [3, 7, 1, 9, 4, 2]
smallest, largest = find_min_max(numbers)
print(f"Smallest: {smallest}, Largest: {largest}")
