
import random

my_tup = ()
i = 0

while i < 6:
    num = random.randint(1, 10)
    my_tup += num,
    i += 1

print('Your lotto numbers are: ')
# # Print the numbers in tuple format
# print(my_tup)

# Print just the numbers with spaces
for element in my_tup:
    print(element, end=' ')
