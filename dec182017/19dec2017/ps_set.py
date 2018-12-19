# SET is the Colletion of Unordered Element
# If element need to SORT means we need to convert in to list

items1 = [1, 2, 3, 4, 5, 6]
items2 = [1, 3, 5, 10, 9]

x = set(items1)
y = set(items2)

print(x.intersection(y))
print()
print (list(x.intersection(y))) # Listing the intesection of both items
print()
print(x.union(y)) # List of items in both the list of items
print()
print(x.difference(y)) # Unique Element in X will display
print(y - x) # Unique in Y compare with X
