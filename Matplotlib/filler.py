import math
import random
import time


maxAmount =  100
current = 0
x = 0

while(current < maxAmount):
    f = open("data.txt", "a+")
    x += 1
    y = int(x*random.random())
    f.write("%s,%s\n" % (x,y))
    time.sleep(1)
    f.close()

