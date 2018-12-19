# Once it defined cannot be modified
# () paranthesis is not important

#items = ('2.2', 2.2, 2, 'eva', 'tim', 'tom', 'jeo')
items = '2.2', 2.2, 2, 'eva', 'tim', 'tom', 'jeo'

n = (1000,)  # Sigle Element represent in Tuple eg: n = 1000,
print(type(n))
print(n)
print()


print(items)

print(type(items))

# Items[-3] = 'timmy'. Printing indexed value
print(items[-3])
print(items[:-3])

for item in items:
    print(item)

