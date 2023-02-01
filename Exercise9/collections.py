# list - mutable ordered collection, positions start at 0

my_list = [1, 2, 3, 4]
print(my_list)

print(my_list[2])
# changing the item in position 2 (third item) as lists are mutable (changeable)
my_list[2] = -4
print(my_list)

# add to the list
my_list.append(9)
print(my_list)

# You can have many variable types or collections within a list i.e. a list within a list
my_second_list = [1, 'Martina', [2, 4, 6]]
print(type(my_second_list))
# selecting a position within the nested list
print(my_second_list[2][1])

# tuple - immutable ordered collection, positions start at 0
my_tuple = (1, 2, 3)
print(type(my_tuple))
print(my_tuple[1])

# set - mutable, unordered; UNIQUE elements
# useful to filter duplicate items by transferring to and from a list
my_set = {1, 2, 3}
print(type(my_set))
my_set.add(7)
print(my_set)
my_set.add(1)
print(my_set)
# UNORDERED

# dictionaries - key value pairs, unordered, access via keys rather than positions
my_dict = { 'first_name' : 'Martina', 'last_name' : 'Yusuf', 'address' : 'Brighton'}
print(my_dict['first_name'])
