import os

file_path = 'column'

# Check if the file or directory exists
if os.path.exists(file_path):
    print(f"'{file_path}' exists.")
else:
    print(f"'{file_path}' does not exist.")
