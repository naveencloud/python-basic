# String Tokanization which will spilt the String Based on the Delimeter Specified

s = 'root:x:0:0:root:1:/root:/bin/bash'
delimiter = ':' # Only One delimiter only possible, we need to use Regular expression to use more delimiters

#Str - Tok
items = s.split(delimiter)
print(items)
print()

print(s.split(delimiter)[0]) #Printing only the Indexed Item
print()

print(s.split(delimiter)[1:]) # Slicing and print the indexed item

# To list the items iteration
for item in items:
    print(item)