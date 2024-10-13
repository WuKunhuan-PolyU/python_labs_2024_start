# Creating a list
fruits = ["apple", "banana", "cherry"]
print("Original list:", fruits)

# Accessing elements
print("First fruit:", fruits[0])
print("Second fruit:", fruits[1])
print("Third fruit:", fruits[2])

# Modifying elements
fruits[1] = "blueberry"
print("Modified list:", fruits)

# Adding elements
fruits.append("orange")
print("List after appending:", fruits)

# Removing elements
fruits.remove("cherry")
print("List after removing 'cherry':", fruits)

# Slicing a list
print("Sliced list (first two elements):", fruits[:2])

# List length
print("Length of the list:", len(fruits))

# Iterating through a list
print("Iterating through the list:")
for fruit in fruits:
    print(fruit)

# List comprehension
uppercase_fruits = [fruit.upper() for fruit in fruits]
print("Uppercase fruits:", uppercase_fruits)