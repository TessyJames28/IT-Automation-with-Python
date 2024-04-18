import os, datetime
# 1.Question 1: The create_python_script function creates a new python script in the current working directory, adds the line of comments to it declared  by the 'comments' variable, and returns the size of the new file. Fill in the gaps to create a script called "program.py".

def create_python_script(filename):
  comments = "# Start of a new Python program"
  with open(filename, 'w') as file:
    file.write(comments)
  filesize = os.path.getsize(filename)
  return(filesize)

print(create_python_script("program.py"))


# 2.Question 2: The new_directory function creates a new directory inside the current working directory, then creates a new empty file inside the new directory, and returns the list of files in that directory. Fill in the gaps to create a file "script.py" in the directory "PythonPrograms". 

def new_directory(directory, filename):
  # Before creating a new directory, check to see if it already exists
  if os.path.isdir(directory) == False:
    new_dir = os.path.join(os.getcwd(), directory)
    os.mkdir(new_dir)

  # Create the new file inside of the new directory
  os.chdir(new_dir)
  with open (filename, 'w') as file:
    pass

  # Return the list of files in the new directory
  return os.listdir(new_dir)

print(new_directory("PythonPrograms", "script.py"))


# 4.Question 4: The file_date function creates a new file in the current working directory, checks the date that the file was modified, and returns just the date portion of the timestamp in the format of yyyy-mm-dd. Fill in the gaps to create a file called "newfile.txt" and check the date that it was modified.

def file_date(filename):
  # Create the file in the current directory
  with open(filename, 'w') as file:
    pass
  timestamp = os.path.getmtime(filename)
  # Convert the timestamp into a readable format, then into a string
  time = str(datetime.datetime.fromtimestamp(timestamp))
  # Return just the date portion 
  # Hint: how many characters are in “yyyy-mm-dd”? 
  return ("{}".format(time[0:10]))

print(file_date("newfile.txt")) 
# Should be today's date in the format of yyyy-mm-dd


# 