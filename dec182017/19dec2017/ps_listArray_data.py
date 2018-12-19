
# List of items need to be defined in Square Bracket []

items = []
print(items)
print(type(items))
print(len(items))
print()

items = [2.2, 'pam', 'allen', 3.3, 'pip', 1.9, 'cpan', 3.4]
print(items)
print()
#Update an element in the list
items[-4] = 'Naveen'
print(items)
print()

#append
items.append('sonic')
print(items)
print()

#insert
items.insert(0, 'bangalore')
items[2] += 'bangalore'  # Appending the string with the exisitng value usinf '+='
print(items)