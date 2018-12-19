# While Loop

i = int(input('Enter the Value for i :'))

while i <= 10:
    if i == 1:
        print(i)
    elif i == 2:
        print('I not equal')
    elif i == 5:
        i += 1 # i = i + 1
        continue
    elif i == 7: # while 'i' equal to 7 the while loop need to break
        break
    else:
        print(i)
    i += 1

# Infinite Loop,
# If Zero len string boolen output will be False
# Otherthan '0' interger all are 'True' in the  boolen
while 'peter':
    print('@', end='\t')

while -12.12:
    print('@', end='\t')

# Boolen Condition False in Test Condition
print(bool(''))
print(bool('0'))
print(bool('0.0'))
print(bool('0+0j'))
print(bool([]))   #List
print(bool(()))   # Tuple
print(bool(set())) # dict
print(bool(None))  # set
print(type(None))