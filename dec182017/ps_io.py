#demo of IO

name = input('enter your name:')
city = input('which area:')
#zip_code = (input('enter the postal code:'))

zip_code = int(input('enter the postal code:')) #int need to add to tell the input value is integer and if value is AlphaNumeric it will be an error

print('name:', name)
print('city:', city)
print(zip_code)
print(type(zip_code))

#########################################################
#Code Block Intended by 4 whitespace
try:
    name = input('enter your name:')
    city = input('which area:')
    #zip_code = (input('enter the postal code:'))
    zip_code = int(input('enter the postal code:')) #int need to add to tell the input value is integer and if value is AlphaNumeric it will be an error
    print('name:', name)
    print('city:', city)
    print(zip_code)
    print(type(zip_code))
except ValueError as err:
    print(err)
print('next stat after try except block')

########################################################

