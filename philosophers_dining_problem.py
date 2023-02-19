import time
import sys
from threading import Thread
global forks

'''

Program to visualise a particular solution to the philosophers dining problem

'''

sys.setrecursionlimit(1500)
forks = [True,True,True,True,True]
philosophers = []

class Philosopher:
    def __init__(self,name,position):
        self.name = name
        self.left = position
        if position == 4:
            self.right = 0
        else:
            self.right = position + 1
        self.TimeSinceLastEaten = 0
        self.activity = "Thinking"
        x = Thread(target=self.timer)
        x.start()
    def timer(self):
        self.TimeSinceLastEaten =self.TimeSinceLastEaten +1
        time.sleep(1)
        self.timer()
    def PickUpForks(self):
        global forks
        if forks[self.left] == True and forks[self.right] == True:
            forks[self.left] = False
            forks[self.right] = False
            self.activity = "Eating"
        else:
            self.activity = "Thinking"
    def Status(self):
        print(self.name, "is", self.activity)
        
philosophers.append(Philosopher("Louis",0))
philosophers.append(Philosopher("Rebekah",1))
philosophers.append(Philosopher("Rydian",2))
philosophers.append(Philosopher("Adam",3))
philosophers.append(Philosopher("Max",4))

while True:
    forks = [True,True,True,True,True]
    LargestTime = -1
    for count in range(5):
        if philosophers[count].TimeSinceLastEaten > LargestTime:
            LargestTime = philosophers[count].TimeSinceLastEaten
            first = count
        else:
            pass
    philosophers[first].PickUpForks()
    if first == 4:
        counter = 0
    else:
        counter = first + 1

    while counter != first:
        philosophers[counter].PickUpForks()
        if counter == 4:
            counter = 0
        else:
            counter = counter + 1
    for item in philosophers:
        item.Status()
    time.sleep(2)
    for item in philosophers:
        if item.activity == "Eating":
            item.TimeSinceLastEaten = 0
            item.activity = "Thinking"
        else:
            pass
    print("")
        
