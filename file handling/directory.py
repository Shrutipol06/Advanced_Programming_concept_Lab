import os

#Get Current Working Directory
print("Current Working Directory:")
print(os.getcwd())

#Make a Directory
os.mkdir("Folder")
print("Directory created successfully.")


#List all files and directories
print("\nList of files and directories:")
print(os.listdir())


#Rename a Directory
os.rename("Folder", "NewFolder")
print("\nDirectory renamed successfully.")


#Change Current Working Directory
os.chdir("NewFolder")
print("\nChanged Working Directory:")
print(os.getcwd())


#List files inside the current directory
print("\nFiles and folders inside NewFolder:")
print(os.listdir())


#Change back to previous directory
os.chdir("..")
print("\nChanged back to previous directory:")
print(os.getcwd())


#Remove a Directory
os.rmdir("NewFolder")
print("\nDirectory removed successfully.")