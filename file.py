import os

def get_file_properties(folder_path):
    """
    Retrieves properties (name and size) of all files in the given folder.
    Ignores subdirectories.
    """
    files_info = []  # List to store file details

    for file_name in os.listdir(folder_path):  
        file_path = os.path.join(folder_path, file_name)  # Get full file path

        if os.path.isfile(file_path):  # Ensure it's a file (not a directory)
            files_info.append({
                'name': file_name,
                'size': os.path.getsize(file_path)  # File size in bytes
            })
    
    return files_info

# Get folder path from user input
folder_path = input("Enter folder path: ").strip()  

# Fetch and display file properties
file_list = get_file_properties(folder_path)
for file in file_list:
    print(file)
