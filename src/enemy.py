from src.entity import entity
from colored import fg
import random
class enemy_child(entity):
    # default values for enemy, these get overwritten in the constructor, Inside the Managers __init__ function
    def __init__(self, arg_color = "%s" % fg(1), arg_name = "Enemy", arg_health = 100, arg_damage = 50, arg_defense = 100):
        self.color = arg_color
        self.name = arg_name
        self.health = arg_health
        self.damage = arg_damage
        self.defense = arg_defense
    # prints enemys stats to screen, gets called in the managers render_status
    def render_status(self):
        print(self.color)
        print("\nName: ", self.name)        
        print("Health: ", self.health) 
        print("Damage: ", self.damage) 
        print("Defense: ", self.defense) 
    # option menu for the enemy. this function is called in Managers "enemy_take_turn" function.
    def MakeChoice(self, arg_player):
        option_select = random.randrange(1, 5)
        if option_select == 1:
            self.violate_opponent(self, arg_player)
        elif option_select == 2:
            self.defend_incoming_attack(self)
        elif option_select == 3:
            self.roll_for_damage(self)
        elif option_select == 4:
            self.roll_for_defense(self)
        elif option_select == 5:
            self.eat_apple(self)
        else:
            print("This couldnt possibly happen")
