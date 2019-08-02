import colored
import random

class entity(object):
    # global variables
    name = "entity"
    health = 100
    damage = random.randrange(1, 100)
    defense = random.randrange(1, 50)
    
# instantiate the entity object
    def __init__(self, name, health, damage, defend):
        self.name = name
        self.health = health
        self.damage = damage
        self.defend = defend

    def render_status(self):
        print("\n\nName: ", self.name)        
        print("Health: ", self.health) 
        print("Damage: ", self.damage) 
        print("Defense: ", self.defend) 

    def take_damage(self):
        self.health = self.health - self.damage
        print("remaining health: ", self.health)