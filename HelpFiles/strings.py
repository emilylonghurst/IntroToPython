# # Unicode characters - use \U after quotation marks
# print("\U0001F600")
#
# # or \N{} with the name inside
# print("\N{winking face}")

######################################################################

# to install a module: pip install moduleName

######################################################################

# # doesn't work as I didn't get the same import as Martina but this is how to do it
# import emoji
#
# print(emoji.emojize("Hello from :robot:"))

######################################################################

# # Printing multiple things
#
# a = "World"
# b = "Hello"
# print(b, a, "from Martina")
# print(b, a, "from Martina", sep='*')
#
# # sep is the gap put between each thing that is printed
# # you can change this using sep='thing to replace space')
#
# print(b, a, "from Martina", end="!!!!")
# # changes the end character to be !!!! rather than enter which makes a new line
#
# print("Hello")
#
# for i in range(0, 10):
#     print(i, end=' ')
# print()
# print(5, "+", 3, "=", 8)

#######################################################################

# # strings can be denoted with single or double quotes
# myStr = 'Martina'
# myStr2 = "Martine"
#
# # however, for names like O'Neill, be careful that it doesn't close the quotation marks mid-name!
#
# lastName = "O'Neill"
# lastName2 = 'O"Neill'
# lastName3 = 'O\'Neill'

#########################################################################

# # \n is interpreted as a new line and \t makes a tab space - these can be used in the middle of a string
#
# longString = "fdsjkf\nrsgurhg/tuidrh\ngfdjghdugraa"

#########################################################################

# # raw strings - will print the literal string, nothing is translated into special characters or altered
#
# rawString = r"\U0001F649"
# rawString2 = r"fdsjkf\nrsgurhg/tuidrh\ngfdjghdugraa"
# print(rawString)
# print(rawString2)

#########################################################################

# # strings are IMMUTABLE - they cannot be changed
# name = "Martina" + " " + "Yusuf"
#
# print(name[4])
# # you cannot do name[4] = "y"
#
# # to concatenate strings, use the join() method instead of writing a loop to combine them all

############################################################################
#
# # turning numbers into strings in order to concatenate
#
# a = 5
# b = 6
# print(str(a) + "+" + str(b) + "=" + str(a+b))

# # BETTER METHOD
#
# # interpolated string
#
# a = 5
# b = 6
# result = f"{a} + {b} = {a+b}"
# result2 = "{} + {} = {}".format(a, b, a+b)
# print(result)
# print(result2)

###########################################################################
#
# # STRING METHODS
#
# # str.replace('old', 'new') - replaces a sub-string
#
# myStr = "I like chocolate more than cheese."
# print(myStr.replace("cheese", "wine"))
#
# # you can make a new string which changes something slightly
# newStr = myStr.replace("cheese", "wine")
#
# myList = ["wine", "cheese", "biscuits", "cat food"]
# myStr = ""
#
# # very resource intensive!! always create a new string instead
# for el in myList:
#     myStr += el
# print(myStr)

#################################################################################

# # .find() - tells you in which position your selection is
#
# myStr = "I like chocolate more than cheese."
# print(myStr.find("cheese"))

#############################################################################

# # str.rstrip() - trims empty spaces from string
# # str.title() - makes every word capitalised

##############################################################################

# # Slicing strings
#
# myStr = "I like chocolate more than cheese."
# # [start: end] - end non-inclusive
# print(myStr[2:9])
# # Slicing outside the range doesn't return anything
# print(myStr[9:2])
# # Negative numbers start from the back of the string
# print(myStr[-4: -1])
#
# # I want the whole string apart from the last character
# my_url = "localhost:8080/hello/"
# print(my_url[0:-1])
#
# # leaving the last number black just prints until the end
# print(my_url[5:])
#
# # simple trick to create a copy of a string
# my_url_copy = my_url[:]
# print(my_url[:])

###############################################################################

# # Create a list from a string using .split()
#
# # Splits on each space
# myStr = "I like chocolate more than cheese."
# my_list = myStr.split()
# print(my_list)
#
# # optional parameter -
# my_url = "localhost:8080/hello/"
# my_list2 = my_url.split("/")
# print(my_list2)

###############################################################################

# # Create a string from a list without using a loop
#
# myList = ["wine", "cheese", "biscuits", "cat food"]
# # the character within '' will put that character between the elements
# my_list_string = '-'.join(myList)
# print(my_list_string)
