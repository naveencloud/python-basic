# Replace the String

import re

s = 'root:x::x:0:0:root::/root:/bin/bash'
print(s)
print()
pattern = ':'
replacment = ','

s2 = re.sub(pattern, replacment, s) # Here defining pattern seperatel and calling it
print(s2)
print()

s3 = re.sub('A|E|I|O|U', "*", s2) # It wont change string because Regx are Case Sensitive
print(s3)
print()

s4 = re.sub('A|E|I|O|U', '*', s2, flags=re.I) #Here AEIOU will be replace with '*'
print(s4)
print()
