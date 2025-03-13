numbers = [10, 20, 30, 40, 50, 60, 25]


ascending_order = sorted(numbers)
descending_order = sorted(numbers, reverse=True)


first_element = numbers[0]
last_element = numbers[-1]
middle_element = numbers[len(numbers) // 2]

print("Original list:", numbers)
print("Sorted in ascending order:", ascending_order)
print("Sorted in descending order:", descending_order)
print("First element:", first_element)
print("Last element:", last_element)
print("Middle element:", middle_element)
