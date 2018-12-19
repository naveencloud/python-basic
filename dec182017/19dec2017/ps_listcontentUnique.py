
# SET is a unique collection of Item

seq = [2.2, 'pam', 'pam', 3, 3, 10, 11, 14, 15, 10, 'in', 'in']
uniq = []

for item in seq:
    if item not in uniq:
        uniq.append(item)

print(uniq)

# Alternate Methond using 'set' function
# SET is the Unordered collection of item or Element 
print(set())
print(list(set(seq)))