import os

'''
This function recursively retrieves all files in a directory and 
stores them in a nested dictionary structure, where subdirectories 
are represented as nested dictionaries.
'''

def recursive_dictionary(path='.'):  # Default path is the current directory
    main_dir = {}  # Dictionary to store file structure

    for root, _, files in os.walk(path):  # Recursively traverse all directories
        sub_dir = main_dir  # Reference to the main dictionary

        # Process subdirectories by extracting the relative path
        for part in root[len(path):].strip(os.sep).split(os.sep):  
            sub_dir = sub_dir.setdefault(part, {})  # Create new nested dict for each subdir
        
        # Store file details in the corresponding directory
        for file_name in files:
            file_path = os.path.join(root, file_name)  # Get full file path
            sub_dir[file_name] = {  # Add file properties to the current subdir
                'name': file_name,
                'size': os.path.getsize(file_path)  # File size in bytes
            }

    return main_dir

# Get folder path from user input
folder_path = input("Enter folder path: ").strip()
nested_dict = recursive_dictionary(folder_path)
print(nested_dict)
