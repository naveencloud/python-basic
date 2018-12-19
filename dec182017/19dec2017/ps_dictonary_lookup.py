# Dictonary Method Add, Update, Delete, LookUP,Iterate

info = {
    'host': 'ws1',
    'domain': 'rootcap.in',
    'desc': 'web-server',
    'app': 'apache httd',
    'version': 2.2
}

item = 'version'

if item in info: # Validate Key in Dictonary
    info[item] = 3.6 #update

print(info)
print()

#################3
info['arch'] = 'x86_64' #Adding an Element to dictonary
print(info)
print()

################# Deleting the "Key" value
print('deleting an element from the dictonaty :')
value = info.pop('desc')
print(value)
print()

### Deleting With the User Input
print('Avalable Keys :')
for item in info:
    print("\t", item)

try:  # Execption Handling to print the error
    item_key = input('Choice to Delet :')
    info.pop(item_key)
    print()
    print(info)
except KeyError as err:
    print(err)

##########################################################
# lookup or Read Operation, Reading Key from Dictionary
# Get is Dictonary Method for Graceful lookup

print(info['host'])
print(info['domain'])

print(info.get('app'))
print(info.get('apps', 'Unknow-Key'))

######################################################
#Iterate the Keys in Dictonary to get only Key and Values Seperately

print(info.keys())   # key only output
print(info.values())  # values only
print(info.items()) # Key, values pair of Each element
############################################################################

# Iterating and Getting Crossponding "Key, Value"

for item in info:  # this method we have to iterate every time it will take time for more Object in Dictionary
    print(item, ':', info[item])

for key, value in info.items(): # It will iterate for key and value
    print(key, '->', value)