import time
import random
import sys
from colored import fg, bg, attr
from os import system, name
from src.player import player_child
from src.enemy import enemy_child

class Manager(object):
    game_over = False
    def __init__(self):
        self.game_over = False
        self.enemy_ai = enemy_child("Enemy AI")
        self.player_1 = player_child(input("\n\nENTER YOUR NAME >>> "))

    def game_start(self):
        welcome_screen = """\t===============================================================
        ===============================================================
        =_=_=_=_=_=_=_=_=_=_=_=_ W E L C O M E _=_=_=_=_=_=_=_=_=_=_=_=        
        _=_=_=_=_=_=_=_=_=_=_=_=_=_=_ T O _=_=_=_=_=_=_=_=_=_=_=_=_=_=_        
        -=-=-=-=-=-=-=-=-=-=-=-=-=-= T H E =-=-=-=-=-=-=-=-=-=-=-=-=-=-        
        ___________________________ G A M E ___________________________        
        ===============================================================        
        ==============================================================="""
        for i in welcome_screen:
            sys.stdout.write(i)
            sys.stdout.flush()
            time.sleep(0.008)

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
        try:
            option_select = int(input("""%s\n\t\t\tOPTIONS:
                                1: ----Attack-----
                                2: ----Defend-----
                                3: ----Roll For Damage Buff----
                                4: ----Roll For Defense Buff----
                                5: ----Eat An Apple----
                                Choose: >>>  """ % fg(117)))
            if option_select == 1:
                self.violate_opponent()
            elif option_select == 2:
                self.defend_incoming_attack(self.enemy_ai)
            elif option_select == 3:
                self.player_1.roll_for_damage()
            elif option_select == 4:
                self.player_1.roll_for_defense()
            elif option_select == 5:
                self.player_1.eat_apple()
            else:
                print("You fumble before your enemy. What a disgrace.")
                self.player_1.health = self.player_1.health - 50
                print("-50 hp")
        except ValueError:
            print("\nOops! That was not a valid number. s o r r y . . .      T_T\n")

    def enemy_threat_dmg(self):
        print("%s\nEnemy about to inflict" % fg(130), self.enemy_ai.damage, "Type damage on your ass.")

    def enemy_do_dmg(self, argument):
        self.player_1.health = self.player_1.health - self.enemy_ai.damage
        print("Enemy strikes swiftly, dealing", self.enemy_ai.damage, "attack damage.")
# damage functionality. should be able to manipulate variables from player_child and enemy_child
    def violate_opponent(self):
        self.enemy_ai.health = self.enemy_ai.health - self.player_1.damage
        print(self.enemy_ai.health)
      
    def defend_incoming_attack(self, argument):
        print("Player deflecting ", self.player_1.defense, "Incoming damage")
        calculated_damage_done = self.enemy_ai.damage - self.player_1.defense
        print("Player taking ", calculated_damage_done, "damage")
        self.player_1.take_damage(calculated_damage_done)
        print("Player: ", self.player_1.health, "current health")
