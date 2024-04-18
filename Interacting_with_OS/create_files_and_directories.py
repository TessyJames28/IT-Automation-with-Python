import os

# Get current directory and create a new one
new_dir1 = os.path.join(os.getcwd(), 'test1')
if not os.path.exists(new_dir1):
    os.mkdir(new_dir1)

new_dir2 = os.path.join(os.getcwd(), 'test2')
if not os.path.exists(new_dir2):
    os.mkdir(new_dir2)

# Create a readme file in test1 directory
file = 'Readme.md'
file_path = os.path.join(new_dir1, file)

with open(file_path, 'w') as file:
    file.write('This is a readme file used for testing')

file2 = 'stay.txt'
file_path2 = os.path.join(new_dir1, file2)

with open(file_path2, 'w') as file:
    file.write('This is a file used for testing and will remain in the test1 directory')

# Move the readme file from test1 to test2
# Define the source and destination path, * will be implemented for learning and future reference even though already defined above
src_path = os.path.join(os.getcwd(), 'test1', 'Readme.md')
dest_path = os.path.join(os.getcwd(), 'test2', 'Readme.md')

# Move the file using os.rename() function
os.rename(src_path, dest_path)