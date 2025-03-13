numbers = [10, 20, 30, 40, 50]


numbers.append(60)
numbers.insert(2, 25)

numbers.remove(30)  
removed_element = numbers.pop(3)  


first_element = numbers[0]
last_element = numbers[-1]
middle_element = numbers[len(numbers) // 2]

print("Updated list after removals:", numbers)
print("Removed element with pop():", removed_element)
print("First element:", first_element)
print("Last element:", last_element)
print("Middle element:", middle_element)
