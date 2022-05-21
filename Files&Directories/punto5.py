import os
def parent_directory():
  # Create a relative path to the parent 
  # of the current working directory 
  relative_parent = os.path.join(os.path.join(os.getcwd(),".."))
  os.chdir(relative_parent)
  relative_parent = os.getcwd()

  # Return the absolute path of the parent directory
  return relative_parent

print(parent_directory())