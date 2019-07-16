# Author - Nitesh Singh Munda
# Date   - 15 July 2019
# Usage  - This script can be used to simplify the overhead to drag images to their respective paths in Android Project
import shutil
import os

class Constants:
	SOURCE = "/Users/dunzo/Desktop/source.txt"
	DESTINATION = "/Users/dunzo/Desktop/destination.txt"
	SOURCE_FOLDER = ["hdpi", "mdpi", "xhdpi", "xxhdpi", "xxxhdpi"]
	DESTINATION_FOLDER = ["drawable-hdpi", "drawable-mdpi", "drawable-xhdpi", "drawable-xxhdpi", "drawable-xxxhdpi"]

def read_source_path():
	# print(Constants.SOURCE)
	file = open(Constants.SOURCE, "r")
	path = file.read()
	return path

def read_destination_path():
	# print(Constants.DESTINATION)
	file = open(Constants.DESTINATION, "r")
	path = file.read()
	return path

def main():
	source = read_source_path()
	destination = read_destination_path()

	print("Enter the current Image Folder (Hint : The folder where zeplin/Sketch exported the images) : ")
	current_folder = input()
	print("Enter file name:")
	image_file_name = input()

	print("Enter the destination folder name (e.g. res/res-pnd/res-home/res-map/res-pillion/res-store) : ")
	destination_folder = input()

	# This part will be used for renaming the image file with the input filename
	for file_name_index in range(len(Constants.SOURCE_FOLDER)):
		source_path = source+current_folder+"/"+Constants.SOURCE_FOLDER[file_name_index]+"/"
		arr = os.listdir(source_path)
		filename = ""
		for i in range(len(arr)):
			if ".png" in arr[i]:
				filename = arr[i]

		if ".png" not in filename:
		filename+".png"
		os.chdir(source_path)
		os.rename(filename, image_file_name)
		print("File name is changed to "+image_file_name+" in "+Constants.SOURCE_FOLDER[file_name_index]+" folder.")



	# This part is for copying the file from one folder to another
	for folder_name_index in range(len(Constants.SOURCE_FOLDER)):
		source_path = source+current_folder+"/"+Constants.SOURCE_FOLDER[folder_name_index]+"/"+image_file_name
		destination_path = destination+destination_folder+"/"+Constants.DESTINATION_FOLDER[folder_name_index]+"/"
		new_path = shutil.copy(source_path, destination_path)
		print("File copied from "+source_path+" to "+destination_path)

	print("***Files Copied***")


if __name__ == '__main__':
	main()