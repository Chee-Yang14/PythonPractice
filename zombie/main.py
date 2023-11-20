from Person import Person
from Zombie import Zombie

day = 7
food = 100
ammo = 100



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
    print("There are seven of you guys\n")
    
    for i in people:
        print(f"{i}\n")
    
    
    
    



def spaces():
    print("\n\n\n")
    
main()