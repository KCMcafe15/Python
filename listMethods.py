fruits = ["berries", "apples", "grapes", "oranges"]
vegetables = ["kale", "broccoli", "lettuce"]

# fruits.extend(vegetables)
# print(fruits)  # Output: ['berries', 'apples', 'grapes', 'oranges', 'kale', 'broccoli', 'lettuce']

# vegetables.append(["carrots"])
# print(vegetables)  # Output: [['kale'], 'broccoli', 'lettuce', ['carrots']]

vegetables.sort()
print(vegetables) 

vegetables.sort(reverse=True)
print(vegetables)  

print(fruits.count("grapes"))    # Output: 1
print(fruits.index("berries"))   # Output: 0
try:
    print(fruits.index("bananas"))  # Raises an exception if the element is not in the list.
except ValueError as e:
    print(e)                       # Output: The element bananas is not in the list.        