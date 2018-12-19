# Copying Files
# Here we can Invoke with any number of argume so arguments denotes "*"

def copy_all(*args):
    source_files, target_files = args[:-1], args[-1]   # -1 indicates lastfile in the arguments as output

    with open(target_files, 'w') as fw:   # with open --> to open target files and it store as 'fw'
        for file_name in source_files:
            fw.write(file_name.center(60, '-') + "\n")
            fw.write(open(file_name).read())

            content = open(file_name).read()   #Reading Source Files
            content = content if content.endswith('\n') else content + "\n"   # Checking Newline charachet in end of file and if it not present

            fw.write(content)
            fw.write('-' * 60 + '\n')
    print(args)

copy_all('f1.txt', 'f2.txt', 'output')