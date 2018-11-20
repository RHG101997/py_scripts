import requests
from bs4 import BeautifulSoup
import sys


'''
    This code uses Dictionary.com for the definitions of the words
'''

word = sys.argv[1]
url = "https://www.dictionary.com/browse/" + word
try: 
    r = requests.get(url)
    bs = BeautifulSoup(r.text,'html.parser')
except:
    print("Invalid Reqest")


try:
    #Part of Speech   
    pos = bs.findAll("span", {"class":"luna-pos"})
    print("\n" + word+ ": " + pos[0].text + "\n")


    #Definitions
    lists = bs.findAll("ol")
    definitions =lists[0].findChildren("li", recursive=False)

    for (i,definition) in enumerate(definitions):
        print(str(i+1), definition.text)
except:
    print("Word not Found")
