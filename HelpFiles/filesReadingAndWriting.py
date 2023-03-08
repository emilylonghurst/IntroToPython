

# # Files

#
# # Will open a file for writing, will create one if it doesn't already exist
# # Will clear the document when it runs
# f = open('myFile', 'w')
#
# # Will open a file for reading
# f = open('myFile', 'r')
#
# # Manually close the document
# f.close()

####################################################################################

# Example

# infile = open('myFile', 'r')
#
# # # Read n characters (in text mode)
# # buffer = infile.read()
# # # print(buffer)
# #
# # # Read a line
# # line = infile.readline()
# # # print(line)

####################################################################################

# content = infile.read()
# # print(content)
# #
# # lines1 = content.splitlines()
# # print(lines1)
#
# lines2 = infile.readlines()
# print(lines2)

###############################################################################

# # Best way to read from a file, specially if the file is very big
# # Printing lines using a for loop
#
# for line in open('myFile'):
#     print(line, end='')

###################################################################################

# # Writing into a file
#
# # writing in a string
# f = open('myFile', 'w')
# f.write('This is coming from Python!!')
#
# # or writing in a list
# my_list = ['apples\n', 'bananas\n', 'oranges\n']
# f.writelines(my_list)

###############################################################################

