numbers = [10, 20, 30, 40, 50, 60, 25]


def calculate_sum(lst):
    return sum(lst)


ascending_order = sorted(numbers)
descending_order = sorted(numbers, reverse=True)
reversed_order = list(reversed(numbers))


first_element = numbers[0]
last_element = numbers[-1]
middle_element = numbers[len(numbers) // 2]


total_sum = calculate_sum(numbers)

print("Original list:", numbers)
print("Sorted in ascending order:", ascending_order)
print("Sorted in descending order:", descending_order)
print("Reversed order:", reversed_order)
print("First element:", first_element)
print("Last element:", last_element)
print("Middle element:", middle_element)
print("Sum of elements:", total_sum)
