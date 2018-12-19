#
# Functional Programming Iteration Over String
# MAP function calls Function "tag_it" and pass args to the "tag_it function

n = map(ord, 'Peter Pan')
ascii = list(n)
print(ascii)
print()

"""
112
<ascii char="p">112/</ascii>
"""
# Defining Function 'tag_it'
def tag_it(av):
    return '<ascii char="{}">{}</ascii>'.format(chr(av), av)

# Both Line No 17 and 21 are same function
n = map(tag_it, ascii) # Calling function tag_it back in map function

#Lambda is the used to pass Argument to Function
n = map(lambda av: '<ascii char="{}">{}</ascii>'.format(chr(av), av), ascii)

for tag in n:
    print(tag)
