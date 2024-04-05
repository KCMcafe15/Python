animals = ["bear", "tiger", "lion", "panda", "elephant"]
for x in animals:
    print(x)
print(animals[1:])  # this will print out everything starting from index [0]
print(animals[1:3]) # this will print out index [0] but not index 3
animals[0] = "cat"
print(animals)
