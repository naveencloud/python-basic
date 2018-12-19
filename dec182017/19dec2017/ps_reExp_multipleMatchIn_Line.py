
# Matching Multiple times in a Line

import re

s = 'The Pthon and the perl Scripting'

pattern = 'P.+?N'

for m in re.finditer(pattern, s, re.I):  # re.I Ignore Case Sensitive
    print("match :", m.group())
    print(m.span())

print(re.findall(pattern, s, re.I))

