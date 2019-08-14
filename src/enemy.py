from src.entity import entity
from colored import fg

class enemy_child(entity):
    # global variables might be unnessesary
    name = "Enemy"

    def __init__(self, arg_name = "", arg_health = 100, arg_damage = 50, arg_defense = 100):
        self.name = arg_name
        self.health = arg_health
        self.damage = arg_damage
        self.defense = arg_defense

    def render_status(self):
        print("\n%sName: " % fg(1), self.name)        
        print("%sHealth: "% fg(1), self.health) 
        print("%sDamage: "% fg(1), self.damage) 
        print("%sDefense: "% fg(1), self.defense) 

    def takes_his_turn(self):
        pass

