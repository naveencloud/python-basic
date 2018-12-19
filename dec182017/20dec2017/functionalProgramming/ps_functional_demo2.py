
items = [1, 2, 3, 4, 3, 5, 10, 10]

temp = list()  # Creating Empty List

# Structural Programming
for i in items:
    temp.append(hex(i))

print(temp)
print()

# Functional Programming Iteration Over List

m = map(hex, items)  # map is a function to map object which iterates
print(m)
print(list(m))

# Functional Programming Iteration Over String
n = map(ord, 'Peter Pan')

ascii = list(n)
print(ascii)