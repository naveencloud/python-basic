# Module Subprocess
# Beging of Output b' --> Byte String

import subprocess
op = subprocess.check_output(['ifconfig'])

ipaddress = subprocess.check_output('ifconfig', shell=True) # Explictly Tokenizing the Command Option we need to use Shell
print(ipaddress)

ls_file = subprocess.check_output(['ls', '-l', '-t', '-r', '../../20dec2017']) # Not need to mention "shell=True" while using []

print(ls_file)
print()
print()

print(op) # Output is Byte string
print()

print(op.decode('ascii')) # Converting Byte string to Unicode as python default is "Unicode"

