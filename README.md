# Scripts

Tool - Image Resource Script

About 

This script will be helpful in making the developement process more fast and painless.
By using this script you can just specify the image resource source path and destination
path, and it will just copy that resource from source to the destination and then it will
rename with the filename specified.

# How It Works?

This is a python script which will just copy the image files path from the source folder to the destination folder.
Steps to use the script:

1. There will be two "txt" files i.e. source.txt and destination.txt. You have
   to just copy the path of source files of the folder where sketch/zeplin export the image resource or any other image resource folder
   Then in the destination.txt just copy the android studio folder path where it keeps the image resource 
   (for e.g. /Users/dunzo/Documents/DunzoUser/demo/src/main).
2. Then the script will ask you to enter the source folder name where the image is and also the source image name. This image_name will   rename the image name in soruce and destination both (**IMPORTANT  Make sure to write image_name.png**).
3. Then there is a class Constants which have "SOURCE" and "DESTINATION", you have to change these to the path name of this project and   where you cloned or unzipped.
4. Run the script image_to_resouce_path.py. Using command -> [Python3 image_to_resouce_path.py]  in the terminal.
5. You are good to go.
