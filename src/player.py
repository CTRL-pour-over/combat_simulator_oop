from src.entity import entity

class player_child(entity):
    name = "Default Player"
    experience = 0

    def __init__(self, arg_name = "", arg_health = 100, arg_damage = 50, arg_defense = 50):
        self.name = arg_name
        self.health = arg_health
        self.damage = arg_damage
        self.defense = arg_defense

