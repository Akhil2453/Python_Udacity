import os

def rename_files():
	files_list = os.listdir("/home/akhil/Desktop/Udacity/Python/prank/")
	#print(files_list)
	savedPath = os.getcwd()
	print(savedPath)
	os.chdir("/home/akhil/Desktop/Udacity/Python/prank/")

	for file_name in files_list:
		os.rename(file_name, file_name.translate(None, "0123456789"))

	os.chdir(savedPath)

rename_files()