import re

s = 'hcl25,x:1033:{1111}: pampam:/home/hcl25,/bin/bash'

items = re.split(',|:|:|', s)
print(items)
