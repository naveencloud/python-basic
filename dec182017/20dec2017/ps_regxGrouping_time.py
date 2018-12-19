
import re
from time import ctime

s = 'root:x::x:0:0:{123}:{543}:777:root::/root:/bin/bash'

#\d matched for digits \d{2} --> Match 2 digits
#\D it match everything otherthan Digit
#\\s for
ts = ctime()
print(ts)

pattern = r'\D{3} (\D{3}) (\d\d) \d{2}:\d{2}:\d{2} (\d{4})'

m = re.search(pattern, ts)
#Printing (m.groups())
print(m)     # It will print the Match patterns
print()
print(m.group())
print()
print(m.groups())
print()
print('day of the month :', m.group(2))
print()
print('month :', m.group(1))


pattern = r'\{(\d+)\}' # Denoting patterns as RAW String because it has special character
replacement = r'<\1>'