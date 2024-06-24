#lists
animals = ["dog", "cat", "rabbit"]
print("Animals List:", animals)  # Output: Animals List: ['dog', 'cat', 'rabbit']

# Accessing elements
print("First Animal:", animals[0])  # Output: First Animal: dog

# Adding elements
animals.append("hamster")
print("Updated Animals List:", animals)  # Output: Updated Animals List: ['dog', 'cat', 'rabbit', 'hamster']
#dictionary
person_info = {"name": "John", "age": 30}
print("Person Dictionary:", person_info)  # Output: Person Dictionary: {'name': 'John', 'age': 30}

# Accessing values
print("Name:", person_info["name"])  # Output: Name: John

# Adding key-value pair
person_info["city"] = "San Francisco"
print("Updated Person Dictionary:", person_info)  # Output: Updated Person Dictionary: {'name': 'John', 'age': 30, 'city': 'San Francisco'}
#tuple
coordinates = (50, 100)
print("Coordinates Tuple:", coordinates)  # Output: Coordinates Tuple: (50, 100)

# Accessing elements
print("First Coordinate:", coordinates[0])  # Output: First Coordinate: 50

# Tuples are immutable
# coordinates[0] = 15  # This will raise an error
