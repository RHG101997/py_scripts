import os

#get directory
currDir = os.getcwd()
#get list of every file in the dir
files_In_Dir = os.listdir()



def check_Dir(ext):
    ext = ext.replace('.','')
    #does folder exist
    ext_dir = os.path.join(currDir,ext)
    if os.path.exists(ext_dir):
        print(f'{ext_dir} -> Exists')
    else:
        #make folder if doesnt exist
        os.mkdir(ext_dir)
        print(f'{ext_dir} -> Created')
    return ext_dir





if files_In_Dir:
    for item in files_In_Dir:

        #get the extensions
        dir = os.path.join(currDir, item)
        _file = os.path.splitext(dir)
        ext = _file[1]

        #this will check is is a file
        if os.path.isfile(dir):
            
            if ext != ".py": 
                #move file to new dir(create if doesnt  exist)
                new_dir = os.path.join(check_Dir(ext),item)
                os.rename( dir , new_dir)
        else:
            print(f'{item} -> folder')
else:
    print("No files to sort")







