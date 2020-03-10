import matplotlib.pyplot as plt
import matplotlib.animation as animation

#Setting the plots
fig, graph = plt.subplots()
fig.suptitle("Live Graph Test")


#Updates called based on the interval of animation
def update(i):
    data = open('data.txt', "r").read()
    lines = data.split('\n')
    dataX =[]
    dataY =[]
    for line in lines:
        if len(line) > 1:
            x,y = line.split(',') 
            dataX.append(float(x))
            dataY.append(float(y))
    graph.clear()
    graph.plot(dataX,dataY)

anim = animation.FuncAnimation(fig,update,interval=1000)
plt.show()