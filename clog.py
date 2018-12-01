import os

'''
    c_log basic logging
    Using ASCII escape sequences 
    to print in the console with colors

'''

def log(c,t):
    os.system("")
    print("["+ str(c)+ "m" + t +"[0m")

def warning(t):
    os.system("")
    print("[93"+ "m" + t +"[0m")

def error(t):
    os.system("")
    print("[91"+ "m" + t +"[0m")
