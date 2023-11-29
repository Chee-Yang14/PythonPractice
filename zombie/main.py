from contextlib import nullcontext
import random
import time
from Person import Person
from Zombie import Zombie

day = 1
food = 100
ammo = 100
ammoUsed = 0
foodUsed = 0
zombies = []
dead = []


def main():
    global day
    print("You are stuck in a school with 7 other people.\n"
          + "the school is surrounded by zombies that will attack every day\n"+
          "you must survive for 7 days which by then help will arrive \n"+ 
          "utilize your ammo and food to survive at all cost\n")
    spaces()
    name = input("What is your name ")
    you = Person(name)
    tou = Person("tou")
    chue = Person("chue")
    charled = Person("charled")
    meng = Person("meng")
    toney = Person("toney")
    cameron = Person("cameron")
    peoples = (you,tou,chue,charled,meng,toney,cameron)
    spaces()
    printPeople(peoples)
    
    while(day<8):
        aDay(day,peoples)
        day += 1
        time.sleep(2)
    

def battleReport(peoples):
    global foodUsed
    foodUsed = food - len(peoples)
    print(f"the amount of food used for the day is: {foodUsed}")
    print(f"the amount of ammo used for the day is: {ammoUsed}")
    
    for d in dead:
        if(dead is nullcontext):
            print("no one die")
        else:
            print(f"{d} is dead")
            
    for people in peoples:
        if(people.health<100):
            damage= people.health - 100
            print(f"{people.name} took {damage} damage and is now at {people.health} hp")

def battlesequence(day,peoples):
    print(f"day {day}")
    spawnZombies(zombies)
    battle(peoples,zombies)
    battleReport(peoples)

def aDay(day,peoples):
    if(day==1):
        battlesequence(day,peoples)
    elif(day==2):
        battlesequence(day,peoples)
    elif(day==3):
        battlesequence(day,peoples)
    elif(day==4):
        battlesequence(day,peoples)
    elif(day==5):
        battlesequence(day,peoples)
    elif(day==6):
        battlesequence(day,peoples)
    elif(day==7):
        battlesequence(day,peoples)
        print("congrat you survive")


def battle(peoples, zombies):
    print(f"{len(zombies)} zombies has arrived")
    print("you are about to battle!")
    spaces()
    while(len(zombies)!=0):
        allAttack(peoples,zombies)
        if(len(zombies)!=0):
            print("it reach here if zom = 0")
            zomAttack(peoples,zombies)
        
        if(len(dead)==7):
            print("everybody died you lost!")

def zomAttack(peoples,zombies):
    for i in zombies:
        if(len(peoples)<=0):
            break
        ranPeep = random.randint(0,len(peoples)-1)
        i.attack(peoples[ranPeep])
        if(peoples[ranPeep].health <= 0):
            print(f"{peoples[ranPeep]} has died")
            dead.append(peoples[ranPeep])


def allAttack(peoples,zombies):
    global ammo
    global ammoUsed
    
    print(f"{ammo}")
    print(f"{len(zombies)}")
    
    for i in peoples:
        if(len(zombies)<=0):
            break
        
        ranZom = random.randint(0,len(zombies)-1)
        if(ammo <= 0):
            break
        
        i.attack(zombies[ranZom])
        ammo= ammo-1
        ammoUsed = ammoUsed+1
        if(zombies[ranZom].health == 0):
            print(f"{i.name} attack {zombies[ranZom].name} and killed him")
            zombies.remove(zombies[ranZom])
        
        

def printPeople(people):
    print(f"There are {len(people)} of you guys\n")
    for i in people:
        print(f"{i}\n")
    
def spawnZombies(zombies):
    if(day<2):
        randNum = random.randint(1,10)
    elif(day<5):
        randNum = random.randint(1,50)
    elif(2<day>=5):
        randNum = random.randint(1,20)
    
    for i in range(randNum):
        zombies.append(Zombie("zombie "+str(i)))
    


def spaces():
    print("\n\n")
    
main()