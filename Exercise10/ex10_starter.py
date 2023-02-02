import sys, glob, os

# Get the directory name
if sys.platform == 'win32':
    hdir = os.environ['HOMEPATH']
else:
    hdir = os.environ['HOME']

# Construct a portable wildcard pattern
pattern = os.path.join(hdir,'*')

# TODO: Use the glob.glob() function to obtain the list of filenames

file_list = glob.glob(pattern)
# print(file_list)

# TODO: use os.path.getsize to find each file's size

# for file in file_list:
#     print(os.path.getsize(file))

# TODO: Add a test to only display files that are not zero length

# for file in file_list:
#     if (os.path.getsize(file)) != 0:
#         print(os.path.getsize(file))

# TODO: Remove the leading directory name(s) from each filename before you print it - 
# using os.path.basename()

for file in file_list:
    if (os.path.getsize(file)) != 0:
        print("Basename: " + os.path.basename(file) + "  Size: " + str(os.path.getsize(file)) + " bytes")
