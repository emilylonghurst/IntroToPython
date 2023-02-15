
# COLLECTIONS

#############################################################################################

# # map() takes a list and a function and applies the function to every element in the list

# # STRUCTURE = map(function, list)
#
# my_list = ['1', '4', '6', '10']
#
# list(map(int, my_list))
#
# # map(int, my_list) does the same as this:
#
# for element in my_list:
#     int(element)

#############################################################################################

# # Finds the length of each word in my_other_list using map()
#
# my_other_list = ['milk', 'bread', 'lipstick']
#
# my_len_list = list(map(len, my_other_list))
#
# print(my_len_list)

##############################################################################################

# # Added integers to an existing list (can also use maps)
#
# my_list = ['1', '4', '6', '10']
#
# result = []
#
# for element in my_list:
#     result.append(int(element))
#
# print(result)

##############################################################################################

# # strings behave like tuples, they are immutable - this code below will give an error
#
# my_str = "Martina"
# my_str[4] = "x"
# print(my_str)
#
# # and ...
#
# my_str.replace('i', 'x') # must be assigned a new variable to work

################

# # now the code below works
# my_str = "Martina"
# new_string = my_str.replace('i', 'x')
# print(new_string)

##############################################################################################

# # MATHEMATICAL FUNCTIONS THAT WORK ON COLLECTIONS
#
# # max() - maximum value
# # min() - minimum value
# # len() - number of elements
# # sum() - sums ints (can be in a list, does not work with string or byte objects)
#
# # do not mix ints and stings though as it will not work
#
# my_num_list = [3, 6, 9, 2, 3]
# print(max(my_num_list))

##############################################################################################

# TUPLES

# my_tuple = (5, 7, 2)
# print(my_tuple)
#
# # use a trailing comma to have just one value in a tuple, otherwise it will be classed as an int
# my_tuple_one = (5,)
# print(my_tuple_one)
#
# # can be without the brackets
# my_tuple_one2 = 5,
# print(my_tuple_one2)
#
# # empty tuple
# my_empty_tuple = ()

###############################################################################################

# # unpacking a tuple - assigning tuple elements to variables
# # number of variables must equal the number of elements in tuple
#
# my_tuple = (5, 7, 2)
# a, b, c = my_tuple
#
# print(a, b, c)
#
# # can also be done like this
# a, b, c = 5, 7, 2
# print(a, b, c)
#
# # how to swap variables - VERY PYTHON SPECIFIC
# d = 6
# e = 9
#
# d, e = e, d
#
# print(e)
# print(d)

#############################################################################################

# # LISTS & TUPLES
#
# my_list = ['milk', 'bread', 'chocolate', 'cheese', 'onions']
#
# # indexing from the right hand side using negative numbers
# print(my_list[-1])
#
# # slicing [start position, end position -1]
# print(my_list[2:4])

############################################################################################

# # put one item into a and then the rest into b
#
# my_list = ['milk', 'bread', 'chocolate', 'cheese', 'onions']
#
# a, *b = my_list
#
# print(a)
# print(b)

#####################
#
# # put first item into a, last item into c and the rest into b
#
# my_list = ['milk', 'bread', 'chocolate', 'cheese', 'onions']
#
# a, *b, c = my_list
#
# print(a)
# print(b)
# print(c)

##########################################################################################
#
# # Looping to slice tuples so the ends are separated into variables
#
# t1 = 'cat', 'dog', 'fish', 'camel', 'fox', 'badger'
# t2 = 'hi', 'hello', 'hey', 'good morning'
# for a, *b, c in t1, t2:
#     print(a, b, c)

##########################################################################################

# # Adding items to a list - first in first out (FIFO) and last in last out (LILO)
#
# # Adding to the front of the list
# my_list = ['milk', 'bread', 'chocolate', 'cheese', 'onions']
# my_list[:0] = ['shoes', 'tea']
#
# print(my_list)
#
# # Adding to the back of the list
# # same thing as .append()
# my_list += ['shoes', 'tea']
# print(my_list)
#
# # Insert an element at a certain position (can use a negative number for a position from the back)
# my_list.insert(3, 'rice')
# print(my_list)

##########################################################################################

# # Removing elements from a list
# # .pop()
#
# # Removing last element (can be assigned another variable too
# my_list = ['milk', 'bread', 'chocolate', 'cheese', 'onions']
# last_element = my_list.pop()
#
# print(my_list)
# print(last_element)
#
# # Removing specific element
#
# my_list.pop(3)
# print(my_list)
#
# # if you know the value of the element you want to remove, but not the value, use .remove()
#
# my_list.remove('milk')
# print(my_list)

###########################################################################################

# # SORTING
#
# # modifying initial collection
# # .sort() method
# cheese = ['Cornish Yarg', 'Oke', 'Edam', 'Stilton']
# cheese.sort(key=len)
# print(cheese)
# # can use different keys to sort
#
# # creating a new collection with sorted values
# # sorted() function (built-in like print)
# nums = ['1001', '34', '3', '77', '42', '9', '87']
#
# # sort alphabetically
# new_str = sorted(nums)
# print(new_str)
#
# # sort numerically
# new_num = sorted(nums, key=int)
# print(new_num)

####################################################################################

# # SETS
#
# # sets elements are unique so will only be printed once
# # sets have no notion of positioning
#
# my_set = {4, 7, 2, 4, 7, 2, 5, 6, 8}
# print(my_set)
#
# # do not remove like this within sets as it may change due to lack of positioning
# num = my_set.pop()
# print(num)
# print(my_set)
#
# # removing is done based on value not position within a set
# my_set.discard(7)
# print(my_set)
#
# # adding an element to a set
# my_set.add(-4)
# print(my_set)

#####################################################################################

# # Using Sets to remove items from Lists
#
# # removing duplicates from a list by turning it into a set
# my_list = [4, 7, 2, 4, 7, 2, 5, 6, 8]
# new_list = list(set(my_list))
#
# print(my_list)
# print(new_list)

################
#
# # remove several items from a list
# my_list = ['milk', 'bread', 'chocolate', 'cheese', 'onions']
# new_list = list(set(my_list) - {'milk', 'chocolate'})
#
# print(my_list)
# print(new_list)

####################################################################################

# # DICTIONARIES
# # to access a certain element you have to use its key not its value
# # keys must be unique
#
# my_dict = {'key1':'value1', 'key2':'value2'}
# print(my_dict['key1'])
#
# # Adding a new element
# my_dict['key3'] = 'value3'
#
# # method .keys() will return a set of keys (as there is no positioning)
# print(my_dict.keys())
#
# # removing an element
# my_dict.pop('key2')
# print(my_dict)

###################################################################################