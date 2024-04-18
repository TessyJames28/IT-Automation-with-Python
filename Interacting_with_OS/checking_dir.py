import os

os.chdir('..')
directory = os.getcwd() # get the current directory

# Loop through and check content for directories and files
for name in os.listdir(directory):
    fullname = os.path.join(directory, name) # use to create a full path that works across all OS
    if os.path.isdir(fullname):
        print(f"{fullname} is a directory")
    else:
        print(f"{fullname} is a file.")