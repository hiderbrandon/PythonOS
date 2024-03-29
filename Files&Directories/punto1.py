'''
The create_python_script function creates a new python script 
in the current working directory, adds the line of comments to it
declared  by the 'comments' variable, and returns the size of the new file.
'''
import os

def create_python_script(filename):
  comments = "# Start of a new Python program"
  with open(filename , "a" ) as theFile:
    print(f"{comments}" ,file=theFile)
  
  filesize = os.path.getsize(filename)
  return(filesize - 1)

print(create_python_script("program.py"))
