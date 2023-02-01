import sys, glob, os

# Get the directory name
if sys.platform == 'win32':
    hdir = os.environ['HOMEPATH']
else:
    hdir = os.environ['HOME']

# Construct a portable wildcard pattern
pattern = os.path.join(hdir,'*')

# TODO: Use the glob.glob() function to obtain the list of filenames

files = glob.glob(pattern)
print(files)
# print(pattern)

# TODO: use os.path.getsize to find each file's size

# file_size = os.path.getsize(files)

# for e in files:
#     print(os.path.getsize(e))

# TODO: Add a test to only display files that are not zero length

for e in files:
    if (os.path.getsize(e)) != 0:
        print("Basename: " + os.path.basename(e) + "  Size: " + str(os.path.getsize(e)) + " bytes")


# TODO: Remove the leading directory name(s) from each filename before you print it - 
# using os.path.basename()
