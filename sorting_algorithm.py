from tkinter import *
import random
import time

'''
Program to visualise bubble sort, insersion sort, and bogo sort on a set of
randomised length bars
'''

root = Tk()
width = 1920
height = 1000
canvas = Canvas(root,width = width,height = height)
canvas.pack()

class bar:
    def __init__ (self,position, length,canvas,num,width):
        self.colour = "black"
        self.xcoordinates =[]
        self.width= width
        start = 5
        for count in range(num):
            self.xcoordinates.append(start)
            start = start + self.width/num
        self.num = num
        #self.xcoordinates =[5,55,105,155,205,255,305,355,405,455]
        self.canvas = canvas
        self.position = position
        self.length = length
        self.object = 0
        self.render()
    def render(self):
        self.canvas.delete(self.object)
        self.object = self.canvas.create_rectangle(self.xcoordinates[self.position],10,self.xcoordinates[self.position]+(self.width-200)/self.num,10+self.length,fill = self.colour)

class counter:
    def __init__(self,canvas,width,height):
        self.canvas = canvas
        self.x = width / 2
        self.y = height - 20
        self.size = 30
        self.counter = 0
        self.text = self.canvas.create_text(self.x,self.y,text = self.counter,fill = "red",font = ("Comic_Sans",self.size))
    def draw(self):
        self.canvas.itemconfig(self.text, text= self.counter)
        root.update()
        
num = 500
global items
items=[]
for count in range(num):
    items.append(bar(count,random.randint(0,height-20),canvas,num,width))
global comparisons
comparisons = counter(canvas,width,height)

def BogoSort(event):
    '''
    input: event of button 2 pressed
    output: sorts bars using bogo sort
    '''
    global items
    global comparisons
    sort = False
    while sort == False:
        comparisons.counter = comparisons.counter + 1
        comparisons.draw()
        length = len(items)
        random.shuffle(items)
        for item in range(length):
            items[item].position = item
            items[item].render()
        root.update()
        #time.sleep(0.1)
        order = True
        n = 0
        while order == True and n < length:
            if items[n].length < items[n+1].length:
                n = n + 1
            else:
                order = False
        if order == True:
            sort = True
        else:
            pass
    Finsih()
    

    
def InsertionSort(event):
    '''
    input: event button 1 is pressed
    output: sorts bars by insersion sort
    '''
    global items
    global comparisons
    for p in range(len(items)):
        hole = items[p]
        hole.colour = "green"
        z = p
        while z > 0 and items[z-1].length > hole.length:
            comparisons.counter = comparisons.counter + 1
            comparisons.draw()
            items[z] = items[z-1]
            items[z].position = z
            items[z].render()
            hole.position = z - 1
            hole.render()
            z = z - 1
            root.update()
            #time.sleep(0.1)
        items[z] = hole
        items[z].colour = "black"
        items[z].render()
    Finish()
                   
def BubbleSort(event):
    '''
    input: event button 3 is pressed
    output: bars are sorted by bubble sort
    '''
    global items
    global comparisons
    for count in range(len(items)):
        I = 0
        Iprevious = 0
        Count = 0
        while Count != (len(items)-1):
            passed = False
            while I != (len(items)-1):
                if items[I].length > items[I+1].length:
                    comparisons.counter = comparisons.counter + 1
                    comparisons.draw()
                    items[I].position = items[I].position + 1
                    items[I+1].position = items[I+1].position - 1
                    temp = items[I+1]
                    items[I+1] = items[I]
                    items[I] = temp
                    items[I].render()
                    items[I+1].render()
                    I = I + 1
                    passed = True
                    #time.sleep(0.00001)
                    root.update()
                else:
                    I = len(items)-1
            Count = Count + 1
            if passed == True:
                I = Iprevious
                Iprevious = Iprevious
            else:
                I = Iprevious + 1
                Iprevious = Iprevious + 1
    Finish()

def Finish():
    global items
    for item in items:
        item.colour = "green"
        item.render()
        root.update()
        time.sleep(0.01)
                
canvas.bind("<Button-2>",BogoSort)
canvas.bind("<Button-1>",InsertionSort)
canvas.bind("<Button-3>",BubbleSort)
root.mainloop()
