numbers = [1, 2, 3, 4]
table = {"field1": 1, "field2": 2, "field3": 3, "field4": 4}

print(type(numbers) is list)
print(type(table) is list)

print(isinstance(numbers, list))  # True
print(isinstance(table, list))  # False
