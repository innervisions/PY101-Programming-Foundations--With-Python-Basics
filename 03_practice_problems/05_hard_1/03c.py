def mess_with_vars(one, two, three):
    one[0] = "two"
    two[0] = "three"
    three[0] = "one"


one = ["one"]
two = ["two"]
three = ["three"]

mess_with_vars(one, two, three)

print(f"one is: {one}")     #["two"]
print(f"two is: {two}")     #["three"]
print(f"three is: {three}") #["one"]
