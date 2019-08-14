from src.entity import entity
from colored import fg
class player_child(entity):
    name = "Default Player"
    experience = 0

    def __init__(self, arg_name = "", arg_health = 100, arg_damage = 50, arg_defense = 50):
        self.name = arg_name
        self.health = arg_health
        self.damage = arg_damage
        self.defense = arg_defense

    def render_status(self):
        print("\n%sName: " % fg(2), self.name)        
        print("%sHealth: "% fg(2), self.health) 
        print("%sDamage: "% fg(2), self.damage) 
        print("%sDefense: "% fg(2), self.defense) 
