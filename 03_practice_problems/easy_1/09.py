advice = "Few things in life are as important as house training your pet dinosaur."
# Expected output:
# Few things in life are as important as
# words = advice.split()
# house_index = words.index("house")
# new_str = " ".join(words[0:house_index])

print(advice.split("house")[0])
