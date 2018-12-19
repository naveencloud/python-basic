# Matching Srting pattern from Multiple Files

import re

file_name1 = 'file1.txt'

fp = open(file_name1, 'r')
pattern = 'p.+?N'

for m in re.search(pattern, file_name1):


fp.close()