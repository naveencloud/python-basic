# File reading and Processing

file_name = 'password.txt' # File Location passing as variable
fp = open(file_name, 'r')

#while True:
#    line = fp.readline()
#    if not line:
#        break
#print(line)

#for item in fp:
 #   print(item) # While Printing it will append the New Line, In Source File already an New Line
  #  print(item, end='') # It will delete the Newline print

#print(fp.read(8))#  Print First 8 bytes
#print(fp.read()) # It will print all

#print(fp.readline()) # It will read the fierst line only

fp.close()