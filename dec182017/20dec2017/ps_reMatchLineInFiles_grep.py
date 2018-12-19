# Fileinput module has capablity equal to SED and AWK
# Modifying the Output in to RED Color txt

import re
from fileinput import  input, filename, filelineno  # input is the function in "fileinput" module

RED = '\033[91m' # Font changing in the Python Output
END = '\033[0m'

def grep_me(pattern, file_names):  # Function Name and Attrbutes
    for line in input(file_names):
        if re.search(pattern, line, re.I):
            content = "{}:{}{}{}:{}".format(filename(), RED, filelineno(), line, END) # It indicates output will be formend by 5 parts {}{}{}{}{}
            print(content, end='')


grep_me('is', ['../19dec2017/file1.txt'])  #searching "python" word in fiel1.txt file



