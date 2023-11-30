from contextlib import nullcontext
import random
import sys
import time
from Person import Person
from Zombie import Zombie

class Day:
    def __init__(self):
        self.day_number = 1
        self.food = 100
        self.ammo = 100
        self.ammo_used = 0
        self.food_used = 0
        self.zombies = []
        self.dead = []
        self.health_potions = 5 

def main():
    # Create an instance of the Day class
    game_day = Day()

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
    peoples = [you, tou, chue, charled, meng, toney, cameron]
    spaces()
    print_people(peoples)

    for day in range(1, 8):
        input("Press Enter to start Day {}...".format(day))
        battle_sequence(game_day, peoples)
    
    print("Congratulations, you survived!")

def battle_report(game_day, peoples):
    game_day.food_used = game_day.food - len(peoples)
    print(f"the amount of food left is: {game_day.food_used}")
    print(f"the amount of ammo used for the day is: {game_day.ammo_used}")

    if not game_day.dead:
        print("No one died.")
    else:
        for d in game_day.dead:
            print(f"{d} is dead")

    for person in peoples:
        if person.health < 100:
            damage = person.health - 100
            print(f"{person.name} took {damage} damage and is now at {person.health} hp")


def use_health_potion(game_day, person):
    person.health += 50
    if person.health > 100:
        person.health = 100
    game_day.health_potions -= 1
    print(f"{person.name} used a health potion. Current health: {person.health}")
    print(f"Remaining health potions: {game_day.health_potions}")


def battle_sequence(game_day, peoples):
    spaces()
    print(f"Day {game_day.day_number}")
    spawn_zombies(game_day.zombies, game_day.day_number)
    battle(peoples, game_day.zombies, game_day)
    rand_num = get_rand_num()
    battle_report(game_day, peoples)
    use_health_potion_prompt(game_day, peoples, rand_num)
    game_day.day_number += 1

def get_rand_num():
    return random.randint(1, 20)  # Replace this with your actual logic for getting rand_num

def use_health_potion_prompt(game_day, peoples, rand_num):
    response = input("Do you want to use a health potion? (yes/no): ").lower()
    if response == "yes" and game_day.health_potions > 0:
        person_choice = input("On whom do you want to use the health potion? Enter the name: ")
        for person in peoples:
            if person.name.lower() == person_choice.lower() and person.health < 100:
                use_health_potion(game_day, person)
                break
        else:
            print("Invalid choice or the person is already at full health.")


def a_day(game_day, peoples):
    battle_sequence(game_day, peoples)

def battle(peoples, zombies, game_day):
    print(f"{len(zombies)} zombies has arrived")
    print("you are about to battle!")
    spaces()
    while len(zombies) != 0 and len(game_day.dead) < 8:
        all_attack(peoples, zombies, game_day)
        if len(zombies) != 0:
            zom_attack(peoples, zombies, game_day)

        if len(game_day.dead) == 7:
            print("everybody died, you lost!")
            sys.exit()
            
def zom_attack(peoples, zombies, game_day):
    zombies_copy = zombies.copy()  # Create a copy of the original zombies list
    for i in zombies_copy:
        if len(game_day.dead) >= 7:
            break
        ran_peep = random.randint(1,len(peoples) - 1)
        person = peoples[ran_peep]

        # Introduce a chance for the zombie to miss (e.g., 20% chance)
        chance_to_miss = random.randint(1,100)
        if chance_to_miss <= 50:
            print(f"{i.name} missed {person.name}!")
            continue

        i.attack(person)
        if person.health <= 0:
            print(f"{person.name} has died")
            game_day.dead.append(person)
            peoples.remove(person)

        # Modify the original zombies list
        zombies.remove(i)


def all_attack(peoples, zombies, game_day):
    for i in peoples:
        if len(zombies) <= 0:
            break

        ran_zom = random.randint(0, len(zombies) - 1)
        if game_day.ammo <= 0:
            break

        i.attack(zombies[ran_zom])
        game_day.ammo -= 1
        game_day.ammo_used += 1
        if zombies[ran_zom].health == 0:
            print(f"{i.name} attack {zombies[ran_zom].name} and killed him")
            zombies.remove(zombies[ran_zom])

def print_people(people):
    print(f"There are {len(people)} of you guys\n")
    for i in people:
        print(f"{i}\n")

def spawn_zombies(zombies, day_number):
    rand_num =0
    if day_number <= 2:
        rand_num = random.randint(10, 20)
    elif day_number <= 5:
        rand_num = random.randint(15, 35)
    elif day_number <= 7:
        rand_num = random.randint(20, 50)

    for i in range(rand_num):
        zombies.append(Zombie("zombie " + str(i)))

def spaces():
    print("\n")

main()
