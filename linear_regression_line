from tkinter import *
import random
import math
import time

'''

Program to estimate a linear regression line given an input of points

'''

def point (x,y,colour):
'''
inputs : coordinates x,y and colour of points

output : draws input points on screen
'''
    canvas.create_oval(x-1,y-1,x+1,y+1,fill= colour)

def Distance( x,y,xaver,yaver,m):
'''
inputs: x, y coordinates. xaver,yaver coordinate averages. m is gradient of line being tested

outputs: calculates the shortest distance from the point inputed and the line outputted 
'''
    liney = 500-(m*(x-xaver)+yaver)
    distance = int(y - liney)
    distance = math.sqrt(distance**2)
    return distance

def DrawLine (x,y,m):
'''
inputs: coordinates x and y, gradient m

outputs: draws line with gradient m on screen
'''
    startx = 0
    while 500-(m*(startx-xaver)+yaver) < 0:
        startx =startx+1
        
    endx = 500
    while 500-(m*(endx-xaver)+yaver) < 0:
        endx = endx-1
    
    line = canvas.create_line(startx,500-(m*(startx-xaver)+yaver),endx,500-(m*(endx-xaver)+yaver),fill ="Red")
    root.update()
    return line


def Gradient_Test (x,y,xaver,yaver):
'''
inputs: x,y (coordinate arrays), xaver,yaver (average values)

outputs: finds the gradient of the linear line with the least cumulative distance from all points
'''
    shortestdistance = 9999999
    #for n in range (0,50,10):
    #loop to get more refined each time
    for m in range(-100,100):
        cumulativedistance = 0
        line = DrawLine (xaver,yaver,m)
 
        for coords in range(len(x)):
            cumulativedistance = cumulativedistance + Distance(x[coords],y[coords],xaver,yaver,m)
        if cumulativedistance < shortestdistance:
            shortestdistance = cumulativedistance
            shortestgradient = m
        else:
            pass
        canvas.delete(line)
    DrawLine (xaver,yaver,shortestgradient)

        
    
x =[]
y =[]

root = Tk()
canvas = Canvas(root,width = 500,height = 500)
canvas.pack()

difference = [2,-2,5,-5,6,-7,3,-1]
for xx in range(1,499):
    x.append(xx)
    y.append(500-(xx+difference[random.randint(0,7)]))

xcum =0
ycum =0
# This example takes an input of points that are generated to have an 'obvious' correlation

for count in range(498):
    point(x[count],y[count],"Black")
    xcum = xcum + x[count]
    ycum = ycum +y[count]

 
xaver = int(xcum/498)
yaver = int(ycum/498)
point(xaver,yaver,"Yellow")

root.bind("<Button-1>",lambda event: Gradient_Test(x,y,xaver,yaver))

root.mainloop()
