import colored
import random

class entity(object):
    # global variables // might wanna remove these
    name = "entity"
    
    
# instantiate the entity object
    def __init__(self, name = "Default Entity", health = 100, damage = random.randrange(1, 100), defense = random.randrange(1, 100)):
        self.name = name
        self.health = health
        self.damage = damage
        self.defense = defense

    def render_status(self):
        print("\n\nName: ", self.name)        
        print("Health: ", self.health) 
        print("Damage: ", self.damage) 
        print("Defense: ", self.defense) 

    def take_damage(self, arg_damage_taken):
        self.health = self.health - self.damage
        print("remaining health: ", self.health)

# A function for damage and defense must exist. Having --random.randrange(1, 100)-- does not work properly when stored as an entity variable. 
# Once the object is initialized, the random integer is stored permenantly. Each entity needs to have a random amount of damage for each round.
    def roll_for_damage(self):
        self.damage = random.randrange(1, 100)
        print("New Damage Stat: ", self.damage)

    def roll_for_defense(self):
        self.defense = random.randrange(1, 100)
        print("New Defense Stat: ", self.defense)

    def eat_apple(self):
        calculated_health_buff = self.health + random.randrange(-25, 200)
        print("calculated_health_buff: ", calculated_health_buff)
        print('mmm, that was tasty. ', self.health, "+", calculated_health_buff, "hp")
        self.health = calculated_health_buff
        print(self.health)
