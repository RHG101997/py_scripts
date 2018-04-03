import os
import argparse




'''
Functions:

check_Dir(ext, *log) -> Check if a folder called with name of the extensions exist(if not it will create it)
ch_Dir(path) -> will chanage the directory that will be sorted
sort_files(args) -> this function will do most of the work
                    ex: call othe functions in order in which they are needed
                    and perform the actual movement of the file
get_args() -> will parse the argumnets, and other options
'''

def check_Dir(current_dir ,ext, log):
    ext = ext.replace('.','') #take the "." out of the extension
    #does folder exist
    ext_dir = os.path.join(current_dir,ext)
    if os.path.exists(ext_dir):   
        if log: print(f'{ext_dir} -> Exists')
    else:
        #make folder if doesnt exist
        os.mkdir(ext_dir)
        if log: print(f'{ext_dir} -> Created')
    return ext_dir #return directory where file should be moved


def ch_Dir(path):
    os.chdir(path)


def sort_files(args):
    if args.path:
        ch_Dir(args.path)
    #get directory
    currDir = os.getcwd()
    #get list of every file in the dir
    files_In_Dir = os.listdir()
    if files_In_Dir:
        for item in files_In_Dir:  
            #get the extensions
            dir = os.path.join(currDir, item) 
            _file = os.path.splitext(dir) 
            ext = _file[1]
            #this will check is a file
            if os.path.isfile(dir):
                    
                if ext != ".py": 
                    #move file to new dir(create if doesnt  exist)
                    new_dir = os.path.join(check_Dir(currDir,ext, args.log),item)
                    if args.log: print(f'{item} -> Moved\n')
                    os.rename( dir , new_dir)
                else:
                    if args.log: print(f'{item} -> Not moved')
    else:
        print("No files to sort")


def get_args():
    parser = argparse.ArgumentParser() #using the parser
    #log all the changes made
    parser.add_argument("-l","--log", help="This will log all changes made to the directory", action="store_true")
    #give a different path to sort
    parser.add_argument("-p","--path",type=str, help="This will change the path that will be sorted")
    return  parser.parse_args()

def Main():
    #gets the args
    args = get_args()
    #sorts the files
    sort_files(args)


if __name__ == '__main__':
    Main()





