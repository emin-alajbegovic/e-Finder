# library
import os

# print current working directory 
# for easier orientation
print("Current working directory is: " + os.getcwd())

# list all directories 
# from current directory
print(list(os.listdir()))


# folder path input
print("Enter folder path")
path = os.path.abspath(input())

# for storing size of each
# file
size = 0

# for storing the size of
# the largest file
max_size = 0

# for storing the path to the
# largest file
max_file =""

# walking through the entire folder,
# including subdirectories
for folder, subfolders, files in os.walk(path):
	
	# checking the size of each file
	for file in files:
       
	   	# join all items into string
		size = len(' '.join(file))

		# updating maximum length
		if size>max_size:
			max_size = size
			max_name = file
			max_file = os.path.join( folder, file )

print("The largest file is: " + max_file)
print("The longest name is: " + max_name)
print('Size: '+ str(max_size) + ' characters')