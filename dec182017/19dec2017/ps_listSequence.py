# It extends the elemnt of the content

items = [2.2, 'pam', 'pam', 3, 3, 10, 11, 14, 15, 10, 'in', 'in']
vow = ['pip', 'easy', 'yaml', 'camel', 'ansible']

items.extend('Naveen') # It will add the individula element or char
print(items)
print()

items.extend(vow)
print(items)
print()
# Appending List to Another List

items.append(vow) # Default append returns value is 'None'
print(items)