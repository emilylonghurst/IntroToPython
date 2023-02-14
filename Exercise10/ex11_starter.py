#!/usr/bin/python

Belgium = 'Belgium,10445852,Brussels,737966,Europe,1830,Euro,Catholicism,Dutch,French,German'

# Adding a line of hypens the same length as the Belgium string

# print(len(Belgium))
print('-' * len(Belgium))

# Commas replaced with .'s

print(Belgium.replace(",", "."))

# Splits on each ,

BelgiumString = Belgium.split(',')
# print(type(BelgiumString))
#print(BelgiumString)

print(int(BelgiumString[1]) + int(BelgiumString[3]))