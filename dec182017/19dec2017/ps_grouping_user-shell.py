# Its Grouping User with  respective Shell and represent in "Dictionary Data Type"
#Rstrip ( It will remove the Right most New Line, TAB, Soace etc..,
# Debugger will show the clearly the step by step execution

from pprint import pprint as pp

content = {}  # Empty Dictionary

for line in open('password.txt'):  #File input it iterate line by line in text IO wrap
    user_info = line.rstrip().split(':')  # Removing New Line and split
    user_name, shell = user_info[0], user_info[-1] # take only 0 index and -1 last index in file

    #Print (user_name, shell)  # If not element exist in dictionary it will be come true

    if shell not in content:   #If the Sheel Existing in Contnet it will be a "True" and initial execution it is always true
        content[shell] = []

    content[shell].append(user_name)

#pp(content)

for shell, list_of_user in content.items(): #Items are the "key:value" in the content
    print(shell)
    print("users count :", len(list_of_user)) # \t gives TAB Space

    for user_name in sorted(list_of_user):
        print(user_name)

    print()

