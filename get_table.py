import clog
import requests
from bs4 import BeautifulSoup
import sys

url  =  sys.argv[1]

try:
    r = requests.get(url)
    bs = BeautifulSoup(r.text, "html.parser")
except:
    print("Website not found")

tb = bs.find_all("table")
print(tb)

