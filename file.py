import os
'''
This recursively gives me files present in subdirectories
but in a single list and not in nested dictionary
'''
def get_file_properties(folder_path):
    files_info = []
    for root, _, files in os.walk(folder_path): #recursively gives all files
        
        for file_name in files:
            file_path = os.path.join(root, file_name) #get full file path 

            file_info = {
                "name": file_name,
                "size": os.path.getsize(file_path)
            }
            files_info.append(file_info)

    return files_info

# Testing the function with a specific directory or leaving it empty for the current one

# Get folder path from user input
folder_path = input("Enter folder path: ").strip()

# Fetch and display file properties
file_list = get_file_properties(folder_path)
for file in file_list:
    print(file)
