import os

# Specify the path of the directory
directory_path = '.'  # Current directory. You can change this to any path you want.

# Check if the path exists
if os.path.exists(directory_path):
    print(f"Contents of the directory '{directory_path}':")
    
    # List all files and folders
    for item in os.listdir(directory_path):
        print(item)
else:
    print(f"The directory '{directory_path}' does not exist.")
