import os
print(os.getcwd()) #get current working directory
folder_path = input('Enter folder path')

files = os.listdir(folder_path) #list of files/folder in directory
print(files)

