#! /usr/bin/python3

import os
import sys
import subprocess
from PIL import Image

# Get the list of the file name in the images folder and store it in a file
def get_file_list():
    
    '''Go to the images directory'''
    os.chdir(os.path.dirname(sys.argv[0]))
    os.chdir("images")

    '''List all of the file name and store it in a new file'''
    subprocess.call('ls',stdout=open('../file_name', 'w'))
    
    '''Return to the main directory'''
    os.chdir(os.path.dirname(sys.argv[0]))
    return

# Get the file name and store it in the variable to be processed locally
def file_list():

    list_of_files = []
    
    '''Open the file and store in local variable to be processed locally'''
    with open('file_name','r') as icon:
        for file_name in icon:
            list_of_files.append(file_name.strip())
        icon.close()
    
    '''Remove the temporary file after it has been stored in local variable'''
    os.remove('file_name')
    return tuple(list_of_files)

# Start to Rotate and Scale down the image
def image_processing():

    '''Take the icon file name'''
    icons_list = file_list()

    '''Create a new directory for containing edited file'''
    if not os.path.isdir("icons"):
        os.mkdir("icons")
    
    '''Enter images directory in order to find the file'''
    os.chdir("images")

    '''Edit the image'''
    for icon in icons_list:

        '''Location of the save file'''
        path = os.path.join(os.path.dirname(sys.argv[0]),"icons",icon)
        
        '''Open the file'''
        img = Image.open(icon)

        '''Rotate and scale down the image'''
        new_img = img.rotate(-90).resize((128,128))

        '''Save the new image into the new path'''
        new_img.convert('RGB').save(path,'jpeg')
        img.close()
    return

def main():
    '''Getting the name file of all list'''
    get_file_list()
    image_processing()

if __name__ == '__main__':
    main()