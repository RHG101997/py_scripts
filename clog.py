import os

'''
    c_log basic logging
    Using ASCII escape sequences 
    to print in the console with colors

'''

class Clog:
    def log(self,c,t):
        os.system("")
        print("["+ str(c)+ "m" + t +"[0m")

    def warning(self,t):
        os.system("")
        print("[93"+ "m" + t +"[0m")

    def error(self,t):
        os.system("")
        print("[91"+ "m" + t +"[0m")
