
# Print Multiples of 7 from 1 to 199
values = list(range(1, 199))
print(values)

print()

m = filter(lambda n: n%7==0, values) # Filer print the value only if it True to the Condition
print(list(m))