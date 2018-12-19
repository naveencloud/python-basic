
import re

#s = 'root:x::x:0:0:{123}:{543}:777:{root}:ahb125:/root:/bin/bash'

# \1 represent the match with the first group
#\b word boundary will match for whole word

pattern = r'\b(\d+)\b'  #grouping alias backref
replacement = r'{\1}' # Its for substrution string

#s2 = re.sub(pattern, replacement, s)
#print(s2)

error = 'Mon Dec 18 17:08:42 IST 2017'
######################
# Printing "mm/dd/yyyy

s = re.sub(r'(\d{2})/(\d{2}/(\d{4})', r'\2-\1-\3', error)
print(s)