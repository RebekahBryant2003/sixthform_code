#Calculator
from tkinter import *
root = Tk()

equa = ""

equation =StringVar()
#A StringVar which allows you to update Label
calculation = Label(root,textvariable = equation)
#textvariable means it updates
calculation.grid(columnspan = 4)

def btnPress(num):
    global equa
    #makes variable equa global
    equa = equa + str(num)
    #updates equa with new value of number
    equation.set(equa)
    #updats equation on calculation with new number

def Calculate():
    global equa
    equation.set(str(eval(equa)))
    equa = ""

def Calculate1(event):
    global equa
    equation.set(str(eval(equa)))
    equa = ""
#allows to find equals when pressing enter key

Button1 = Button(root,text="1",command =lambda:btnPress(1))
#lambda is a function with no return (anoynomous function) and allows parameter to be passed)
Button1.grid(row = 1,column = 0)
Button2 = Button(root,text="2",command =lambda:btnPress(2))
Button2.grid(row = 1,column = 1)
Button3 = Button(root,text="3",command =lambda:btnPress(3))
Button3.grid(row = 1,column = 2)
Plus= Button(root,text="+",command =lambda:btnPress('+'))
Plus.grid(row = 1,column = 3)
Times= Button(root,text="*",command =lambda:btnPress('*'))
Times.grid(row = 1,column = 4)




Button4 = Button(root,text="4",command =lambda:btnPress(4))
Button4.grid(row = 2,column = 0)
Button5 = Button(root,text="5",command =lambda:btnPress(5))
Button5.grid(row = 2,column = 1)
Button6 = Button(root,text="6",command =lambda:btnPress(6))
Button6.grid(row = 2,column = 2)
Minus= Button(root,text="-",command =lambda:btnPress('-'))
Minus.grid(row = 2,column = 3)
Divide= Button(root,text="/",command =lambda:btnPress('/'))
Divide.grid(row = 2,column = 4)



Button7 = Button(root,text="7",command =lambda:btnPress(7))
Button7.grid(row = 3,column = 0)
Button8 = Button(root,text="8",command =lambda:btnPress(8))
Button8.grid(row = 3,column = 1)
Button9 = Button(root,text="9",command =lambda:btnPress(9))
Button9.grid(row = 3,column = 2)

Button0 = Button(root,text="0",command =lambda:btnPress(0))
Button0.grid(row = 4,column = 1)
Equals= Button(root,text="=",command = Calculate)
Equals.grid(row = 4,column = 4)
root.bind("<Return>",Calculate1)
#allows you to also press the enter key instead of the equals button


root.mainloop()

