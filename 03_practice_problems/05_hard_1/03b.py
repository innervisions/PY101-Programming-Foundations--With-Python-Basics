def mess_with_vars(one, two, three):
    one = ["two"]
    two = ["three"]
    three = ["one"]

one = ["one"]
two = ["two"]
three = ["three"]

mess_with_vars(one, two, three)

print(f"one is: {one}")     #["one"]
print(f"two is: {two}")     #["two"]
print(f"three is: {three}") # ["three"]
