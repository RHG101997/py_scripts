import sys
import os
import shutil

# if true will log the script
logging = 'false'

def log(string):
    if logging == 'true':
        print(string)

def copy(path_src,path_des):
    # Copy the file
    try:
        log("FROM: " + path_src + " TO: " + path_des)
        shutil.copy(path_src, path_des)   
    except:
        log("File Exists")

def each_file(path_src, path_des):
    
    # This loop will go through every folder and file
    for folderName, subfolders, filenames in os.walk(path_src):
        log('The current folder is ' + folderName)
        # this will create the sub folders in the current folder
        for subfolder in subfolders:
            log('SUBFOLDER OF ' + folderName + ': ' + subfolder)
            try:
                # The current path of the src folder 
                # is replace with the path to new destination
                # before replace: C\\src\\EXAMPLE_FOLDER
                # after replace: C\\des\\EXAMPLE_FOLDER
                new_path = folderName.replace(path_src,path_des)
                os.mkdir(new_path+"\\"+subfolder)
            except:
                log("Folder Exists:" + subfolder)
        for filename in filenames:
            # Every file is copied base on where the 
            # os.walk(path) function is

            # new_path is obtained by using same method of subfolders
            new_path = folderName.replace(path_src,path_des)
            file = folderName + '\\'+ filename
            copy(file, new_path)

'''
    "-d" use current dir as src and destination will be provided
    "-s" use current dir as des and the source will be provided
'''

if sys.argv[1] == "-d":
    each_file(os.getcwd(), sys.argv[2])     
if sys.argv[1] =="-s":
    each_file(sys.argv[2], os.getcwd())
