import requests
from bs4 import BeautifulSoup
import clog # Can be deleted and change to print("")
import os
import sys

'''
    Gets all websites links from google search 
    and shows them to you
    OR
    -o flag: makes the script go to 
    each site and gets all "p" tags and dump it into file
Trying 
    IMPORTANT: this script is a test many websites do not
                work as intented.
'''


url ="https://www.google.com/search?q="
topic = sys.argv[1]
mode = ""
res_sources = requests.get(url+topic)
try:
    # Detecting for the -o parameter
    mode = sys.argv[2]
    if mode == "-o" :
        new_dir = os.getcwd()+"\\"+topic
        # Making new Directory to dump the files
        os.mkdir(new_dir)
        os.chdir(new_dir)
except:
    pass


# this function will go to the link and dump the text into .txt file
def getContent(link,source):
    clog.log(96,"Getting content: ") #-> same as a print
    clog.log(0,"->"+link)
    try:
        content_html = requests.get(link)
        content_parse = BeautifulSoup(content_html.text, "html.parser")
        content = content_parse.find_all("p")
        with open("Source "+ str(source) +".txt", "w") as f:
            for tags in content:
                f.write(tags.get_text())
    except:
        clog.error("Problem getting Content of:" + link)


# This the main part of the script
# gets the links and calls getContent() function

links =  BeautifulSoup(res_sources.text, "html.parser")
sources = links.find_all("cite")
clog.log(93 ,"Sources: ")
sourcesNum = 0
for tags in sources:
    sourcesNum+=1
    if mode == "-o":
        getContent(tags.get_text(), sourcesNum)
    else:
        print("•"+tags.get_text())
        
    
        