# Filter Line with Root
# '$' indicated end of the line in RegEx

import re

pattern = 'bash$'

# Filter Module Execute and we have to iterate through the For loop or Print to Get Output to print
# Filter taks Column oject and Iteratable Object

filter_lines = filter(lambda line: re.search(pattern, line, re.I), open('../../19dec2017/password.txt'))

print(filter_lines)
#for matched_line in filter_lines:
#    print(matched_line, end='') #Each Line in Print is Newline, To trailin NewLine we need to use "end=''"
