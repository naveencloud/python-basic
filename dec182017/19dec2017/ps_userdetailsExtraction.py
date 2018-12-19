# Extracting and Sorting User  with Line Number

file_name = 'password.txt' # File Location passing as variable
fp = open(file_name, 'r')

list_of_users = [] # Empty List defining to store the items

for line in fp:
    user_info = line.split(':')
    list_of_users.append(user_info[0]) # Appending to empty list

fp.close()
#print(list_of_users)
list_of_users.sort()

for item in list_of_users:
    print(item )
print()
print(enumerate(list_of_users))
print()

# Iterate List item for its index, value

for item1, item2 in enumerate(list_of_users, 1):
    print(item1, '->', item2)