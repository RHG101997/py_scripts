import os


# TODO: add bold, underline and inverse support
# TODO: update warning, error fucntion using the genColorCode function
# TODO: create an inline color changing 
# TODO: using [option obj] to save your preferences in the script

class BeginClog:
    '''
    c_log basic logging
    Using ASCII escape sequences 
    to print in the console with colors
    '''
    color_bg ={
        "normal":40,
        "strong":100
    }
    color_text = {  
        "normal":30,
        "strong":90,
    }
    color = {
        "black":0,
        "red":1,
        "green":2,
        "yellow": 3,
        "blue": 4,
        "magenta":5,
        "cyan":6,
        "white":7
        
    }
    def __init__(self):
        # required for color to be correctly displayed
        os.system("")
          


    '''
        ***************************************************************
        ***************    Title(Log) coloring  ***********************
        ***************************************************************
        Log function are like a print, but they have the option to chnage the bg, and also
        they reset the color when they end.

    '''

    def genColorCode(self, text_accent, txt_color, bg_color = "none",bg_accent = "normal"): 
        '''This function is used by c_log class to get the code for the colors [Ex:[91m] '''
        txt_code = 0
        bg_code = 0
        try:
            txt_code = self.color_text[text_accent] + self.color[txt_color]

            if bg_color == "none":
                return "["+ str(txt_code) + "m"
            else:
                bg_code = self.color_bg[bg_accent] + self.color[bg_color]
                return "["+ str(txt_code) +";" + str(bg_code) + "m" 
            
        except:
            # Color will not change
            return ""



    def log(self,color, text, txt_accent = "strong" ): 
        ''' This function accepts the color and the text to be printed [Optional txt Accent]'''     
        color_code = self.genColorCode(txt_accent.lower(),color.lower())
        print(color_code + text + "[0m")

    def bgLog(self, bg_color, txt_color, text, bg_accent="normal"):
        ''' Create text with color and also change the Background color[Optional bg Accent (Visible)]'''
        color_code = self.genColorCode("strong",txt_color.lower(),bg_color.lower(),bg_accent.lower())
        print(color_code + text + "[0m")


    def warning(self,t):
        ''' Print text in yellow color'''
        os.system("")
        print("[93"+ "m" + t +"[0m")

    def error(self,t):
        ''' Print text in red color'''
        os.system("")
        print("[91"+ "m" + t +"[0m")

    '''
        ***************************************************************
        *******************    Block coloring  ***********************
        ***************************************************************
        When function begin is called all text printed after that point
        will be colored base on the color selected
    
    '''
    def beginBlock(self, txt_color):
        color_code = self.color_text["strong"] + self.color[txt_color]
        print("["+ str(color_code) +"m",end="")
    
    def reset(self):
        print("[0m",end="")








def testLogs():
    '''clog.test() To see some results this is Example Code'''
    q = BeginClog()
    # This is using log function
    q.log("red","Red text -  Normal Accent","normal")
    q.log("red","Red text  -  Strong Accent", "strong")

    q.log("yellow","Yellow text Strong Accent(default)")
    q.log("Blue","Blue text Normal Accent","normal")
    q.log("cyan","Cyan Text Default Accent(Strong)")

    # This is using bgLog
    q.bgLog("red","green", "I am greeen with red bg[Accent is normal]")
    q.bgLog("red","green", "I am greeen with red bg[Accent is strong]", "strong")

    q.bgLog("cyan","red", "I am red with cyan bg[Accent is normal]")
    q.bgLog("cyan","red", "I am red with cyan bg[Accent is strong]", "strong")

def testBlock():
    q = BeginClog()
    # this functions will begin a block of colored text
    q.beginBlock("cyan")
    print("This text is colored cyan")
    print("this will be colored cyan")
    # this function will return text to normal
    q.reset()
    print("Now this is not colored")
