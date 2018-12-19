# Indexing, Slicing, Iteration
# 0 1 2 3 4 +ve indexing

# p y t h o n

# 4 3 2 1 0 -ve indexing

s = 'python'

print(s[0])
print(s[1])
print(s[2])
print(s[3])
print(s[4])

print(s[-1])
print(s[-2])
print(s[-3])
print(s[-4])
print(s[-5])

#########################
"""
Slicing

Syntax: name[start-index: ex-of-end-index] --> Itn will stop the before the end-of the index
"""

s = 'Tis is a usefull traing for python'
s2 = s.replace('usefull', 'nice') # New String with replace string and it stored in S2 variable
print(s)

print(s2)
print(s.find('useful'))
print(s.index('useful'))

print(s[:4])
print(s[10:14])
print(s[-5:])
print(s[:])
print(s2[1:-1])
print(s2[-6:-4])

print(s[::-1]) # It reverse a String and it only way to reverse in Python

######### ITERATION #################

s3 = 'Tis is a sample pyhton string iteration function'

for item in s3:   # To iterate we use For in Loop. In every iteration it will take a character and put in 'item'
    print(item)
    print("{} :{}".format(item, ord(item))) # white space ascii value is 32


s4 = 'Tis is a sample pyhton string iteration function'
column_count = 0
for item in s4:   # To iterate we use For in Loop. In every iteration it will take a character and put in 'item'
    if item not in 'aeiou ':  # To avoid printing Vowles and whitespace
        print("{} :{}".format(item, ord(item)), end='\t\t')
    else:
        print('**', end='\t\t')

    column_count += 1

    if column_count == 10:
        print()
        column_count = 0