import time
import random
from colored import fg, bg, attr
from os import system, name
from src.player import player_child
from src.enemy import enemy_child

class Manager(object):
    game_over = False
    def __init__(self):
        self.game_over = False
        self.enemy_ai = enemy_child("Enemy AI", 150, enemy_child.damage, enemy_child.defense)
        self.player_1 = player_child(player_child.name, 100, player_child.damage, player_child.defense)

    def game_start(self):
        print("""\t\t ===============================================================
                 ===============================================================
                 =_=_=_=_=_=_=_=_=_=_=_=_ W E L C O M E _=_=_=_=_=_=_=_=_=_=_=_=
                 _=_=_=_=_=_=_=_=_=_=_=_=_=_=_ T O _=_=_=_=_=_=_=_=_=_=_=_=_=_=_
                 -=-=-=-=-=-=-=-=-=-=-=-=-=-= T H E =-=-=-=-=-=-=-=-=-=-=-=-=-=-
                 ___________________________ G A M E ___________________________
                 ===============================================================
                 ===============================================================""")

    def print_end_screen(self):
        print("""\t\t =
                 ===============================================================
                 =_=_=_=_=_=_=_=_=_=_=_=_=_=_ G A M E _=_=_=_=_=_=_=_=_=_=_=_=
                 _=_=_=_=_=_=_=_=_=_=_=_=_=_ O V E R _=_=_=_=_=_=_=_=_=_=_=_=_=_=_
                 -=-=-=-=-=-=-=-=-=-=-=-=-=-= Y O U =-=-=-=-=-=-=-=-=-=-=-=-=-=-
                 ___________________________ S U C K ___________________________
                 ===============================================================
                 ===============================================================""")

    def clear(self):
        if name == 'nt':
            _ = system('cls')
        else:
            _ = system('clear')

    def render_status(self):
        self.player_1.render_status()
        self.enemy_ai.render_status()

    def input_management(self):
        option_select = int(input("""OPTIONS
                            1: ----Attack-----
                            2: ----Defend-----
                            Choose: >>>  """))
        if option_select == 1:
            self.violate_opponent()
        elif option_select == 2:
            self.defend_incoming_attack(enemy_child)
        else:
            print("You fumble before your enemy. What a disgrace.")
            self.player_1.health = self.player_1.health - 50
            print("-50 hp")
        
# damage functionality. should be able to manipulate variables from player_child and enemy_child
    def violate_opponent(self):
        self.enemy_ai.health = self.enemy_ai.health - self.player_1.damage
        print(self.enemy_ai.health)
      
    def defend_incoming_attack(self, argument):
        print("%s Player deflecting " % (fg(2)), argument.defense)
        argument.damage = argument.damage - player_child.defense
        print("%s Player taking " % (fg(2)), argument.damage)
        player_child.health = player_child.health - argument.damage
        print("%s Player: " % (fg(2)), player_child.health)
