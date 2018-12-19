"""demo for string formatting is for printing the rows and column {:fmt-str}"""

name, age, gender = 'sarah', 3, 'female'  # Variable Parallel assignment

print("|{}|{}|{}|".format(name, age, gender))  # It will print output as directly
print("|{:>22}|{:>9}|{:>20}|".format(name, age, gender)) # It will have the Column width size, output will alligned from right side in column
print("|{:<22}|{:<9}|{:<20}|".format(name, age, gender)) # It will have the Column width size, output will alligned from Lift side in column
print("|{:^22}|{:^9}|{:^20}|".format(name, age, gender)) # # It will have the Column width size, output will alligned from Center side in column
print("|{:22}|{:9}|{:20}|".format(name, age, gender)) # # It will have the Column width size, output will alligned as per data type side in column
print("|{:>22}|{:>9.2f}|{:20}|".format(name, age, gender)) ## It will have the Column width size, output will alligned from right side in column with "floating" in age column