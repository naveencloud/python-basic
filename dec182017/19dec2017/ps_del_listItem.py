
items = [2.2, 'pam', 'allen', 3.3, 'pip', 1.9, 'cpan', 3.4]

# By Index "pop" the element in list "Index"
#POPS the last element by Default

value = items.pop()
print(value)
print(items)
print()

# Delete By Value, By default it will remove the first occurence of the value
items = [2.2, 'pam', 'pam', 3.3, 'pip', 1.9, 'pam', 3.4]
item = 'pam'
items.remove(item)
print(items)

# Deleting the all the required value in List "use While Condition"
items1 = [2.2, 'pam', 'pam', 3.3, 'pip', 1.9, 'pam', 3.4]
ite = 'pam'

print(items1.count(ite)) # To Find the Count of the Element in Array

while ite in items1:
    items1.remove(ite)

print()
print(items1)

# Deleting Only First Occurance of 'pam'. Functions are not available only Work Around

items2 = [2.2, 'pam', 'pam', 3.3, 'pip', 1.9, 'pam', 3.4]

it = 'pam'

first_occurance_pam = items2.index(it) # It will index the value

temp = items2[first_occurance_pam+1:] # It will slice the list and store in Variable
print(temp)
print()
# Below it will remove the value from the sliced
while items2 in temp:
    temp.remove(it)

# It will concatenate the string
print(items2[:first_occurance_pam + 1] + temp)