def ends_in_exclaimation(text: str) -> bool:
    return text[-1] == "!"


str1 = "Come over here!"  # True
str2 = "What's up, Doc?"  # False

print(ends_in_exclaimation(str1))
print(ends_in_exclaimation(str2))

print(str1.endswith("!"))  # True
print(str2.endswith("!"))  # False
