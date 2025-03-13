numbers = [10, 20, 30, 40, 50]


numbers.append(60)
numbers.insert(2, 25)


first_element = numbers[0]
last_element = numbers[-1]
middle_element = numbers[len(numbers) // 2]

print("Updated list:", numbers)
print("First element:", first_element)
print("Last element:", last_element)
print("Middle element:", middle_element)
