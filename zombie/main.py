import random
from Person import Person
from Zombie import Zombie

day = 7
food = 100
ammo = 100
zombies = []
dead = []


def main():
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
    people = (you,tou,chue,charled,meng,toney,cameron)
    spaces()
    printPeople(people)
    
    print("day 1")
    
    spawnZombies(zombies)
    battle(people,zombies)
    
    
    
def battle(peoples, zombies):
    print(f"{len(zombies)} zombies has arrived")
    print("you are about to battle!")
    while(len(zombies)!=0):
        spaces()
        while(len(zombies)!=0):
            allAttack(peoples,zombies)
            if(len(zombies)!=0):
                zomAttack(peoples,zombies)

def zomAttack(peoples,zombies):
    for i in zombies:
        if(len(peoples)<=0):
            break
        ranPeep = random.randint(0,len(peoples)-1)
        i.attack(peoples[ranPeep])
        if(peoples[ranPeep].health == 0):
            print(f"{peoples[ranPeep]} has died")
            dead.append(peoples[ranPeep])
            zombies.remove(zombies[ranPeep])


def allAttack(peoples,zombies):
    for i in peoples:
        if(len(zombies)<=0):
            break
        ranZom = random.randint(0,len(zombies)-1)
        i.attack(zombies[ranZom])
        ammo-1
        if(zombies[ranZom].health == 0):
            print(f"{i.name} attack {zombies[ranZom].name} and killed him")
            zombies.remove(zombies[ranZom])

def printPeople(people):
    print(f"There are {len(people)} of you guys\n")
    for i in people:
        print(f"{i}\n")
    
def spawnZombies(zombies):
    if(day>5):
        randNum = random.randint(1,10)
    elif(day<2):
        randNum = random.randint(1,30)
    else:
        randNum = random.randint(1,20)
    
    for i in range(randNum):
        zombies.append(Zombie("zombie "+str(i)))
    


def spaces():
    print("\n\n")
    
main()