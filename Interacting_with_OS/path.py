import os

# Change to a new directory
new_dir = "C:/Users/USER/Desktop/tessyjames/Exercises"
os.chdir(new_dir)

# Verify the new current directory
current_dir = os.getcwd()
print(current_dir)

# Change to the parent directory
print(os.chdir('..'))

# Change to the home directory
print(os.chdir(os.path.expanduser("~")))

# # Change to a relative path
# print(os.chdir("my_project/src"))

outputs = {}
outputs['current_directory_before'] = os.getcwd()
values = outputs['files_and_directories'] = os.listdir()
for i, dir in enumerate(values):
    print(f"{i:<3}      {dir:>6}")

print(outputs)