
import math
from tkinter import *
import time



"""
This code is designed to visualize and estimate decimals.
"""

def circles(event):
    """
    input: Event Triggered When Enter Bar pressed
    
    output: takes input of a decimal and (starting from centre) draws points, turning that fraction of 360 degrees between each point
    
    """
    canvas.delete("all")
    X = 25
    Y = 25
    nextX = 25
    nextY = 25
    num = int(e.get())
    # fraction = float(frac.get())
    #Retrieves the fraction inputted
    fraction = (1 + 5 ** (1 / 2)) / 2
    #Puts the golden ratio as the fraction
    angle = fraction * 360
    Angle = angle - 90
    radian = math.radians(angle)
    Radian = math.radians(Angle)
    cos = math.sin(Radian) * -1
    sin = math.sin(radian)
    for count in range(num):
        loop(nextX, nextY)
        tempX = X
        enlargement = (count + 2) / (num / 10)
        X = (X * cos) + (Y * (-sin))
        Y = (tempX * sin) + (Y * (cos))
        nextX = enlargement * X
        nextY = enlargement * Y


def loop(nextX:int=None, nextY:int=None): #do type hinting. 
    """
    input: X and Y coordinates

    output: Places oval at X and Y coordinate

    """
    canvas.create_oval(
        nextX + 248, nextY + 248, nextX + 252, nextY + 252, fill="Yellow"
    )

# fraction = float(input("Enter a fraction for the turn:"))
# fraction = (1 + 5**(1/2))/2
root = Tk()

canvas = Canvas(root, width=500, height=500)
canvas.pack()
canvas.create_oval(249, 249, 251, 251, fill="Red")

frac = Entry(root)
frac.pack()

e = Entry(root)
e.pack()

root.bind("<Return>", circles)
root.mainloop()
