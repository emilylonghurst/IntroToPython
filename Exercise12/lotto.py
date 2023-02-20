
import random

my_set = set()

while len(my_set) < 6:
    num = random.randint(1, 10)
    my_set.add(num)

print('Your lotto numbers are: ')

# # Print the numbers in tuple format
# print(my_tup)

# Print just the numbers with spaces
for element in my_set:
    print(element, end=' ')
