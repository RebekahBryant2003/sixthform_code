import time
from threading import Thread
'''
Program like tamagotchi - must take care of your pets
'''
class Pet:
    def __init__ (self,name,breed):
       self.name =name
       self.breed = breed
       self.hunger = 0
       self.intelligence = 0
       self.bored= 0
       self.times = 0
       self.alive = True
       x = Thread(target=self.timer)
       x.start()
    def timer(self):
        time.sleep(0.5)
        self.times = self.times + 1
        self.hunger = self.hunger + 1
        self.bored = self.bored + 1
        if self.hunger == 100 or self.bored == 100:
            self.alive = False
        else:
            self.timer()
    def eat(self):
        self.hunger = 0
    def play(self):
        self.bored = 0
    def read(self):
        self.intelligence = self.intelligence + 1
pets = []
pets.append(Pet("Louis","Meercat"))
pets.append(Pet("Max","Rat"))

end = False
dead = []
while end == False:
    for pet in pets:
        if pet.alive == False:
            end = True
            dead.append(pet)
            pets.remove(pet)
        else:
            end = False   
        print(pet.name,"'s Stats are:")
        print("Hunger: ",pet.hunger,"%")
        print("Bored: ",pet.bored,"%")
        print("Intelligence: ",pet.intelligence)
        choice = int(input("\nWhat would you like to do: \n1)Eat \n2)Play \n3)Read \n"))
        if choice == 1:
            pet.eat()
        elif choice == 2:
            pet.play()
        else:
            pet.read()
    for pet in dead:
        print(pet.name," is dead!")
    time.sleep(0.5)
print("All your pets are dead")
