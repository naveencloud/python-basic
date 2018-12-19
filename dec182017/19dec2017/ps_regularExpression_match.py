# RegExp Matching. It is case Sensitive and it will match only once in a line. It Match for Sub-Sting eg: Sunflower it match with Sun

import re

s = 'The python and the perl scripting'

pattern = 'P.+N' #

patterns = 'P.+?N' # Non-Greedy, Least occurenace to match and print

m = re.search(pattern, s)
print(m)
print()
n = re.search(patterns, s, re.I) # re.I to ignore Case sensitive
print(n)

if n:
    print("match :", n.group())
    before = s[:n.start()] # Print Before the Match content
    after = s[n.end():] #Print content after the match content
    print("before : |{}|".format(before))
    print("after: |{}|".format(after))
else:
    print('Failed to Match')