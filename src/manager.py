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
        ###### CONSTRUCTING THE PLAYER AND ENEMY OBJECTS, ALL DEFAULT VALUES ARE USED EXCEPT FOR NAMES AND COLORS ######
        self.enemy_ai = enemy_child("%s" % fg(1), "Enemy AI")
        self.player_1 = player_child("%s" % fg(2), input("\n\nENTER YOUR NAME >>> "))

    loser_end_screen = """\t\t =
                 ===============================================================
                 =_=_=_=_=_=_=_=_=_=_=_=_=_=_ G A M E _=_=_=_=_=_=_=_=_=_=_=_=_=
                 _=_=_=_=_=_=_=_=_=_=_=_=_=_ O V E R _=_=_=_=_=_=_=_=_=_=_=_=_=_
                 -=-=-=-=-=-=-=-=-=-=-=-=-=-= Y O U =-=-=-=-=-=-=-=-=-=-=-=-=-=-
                 ___________________________ S U C K ___________________________
                 ==============================================================="""
    
    winner_end_screen = """===============================================================
                 =_=_=_=_=_=_=_=_=_=_=_=_=_=_ F A M E _=_=_=_=_=_=_=_=_=_=_=_=_=
                 _=_=_=_=_=_=_=_=_=_=_=_=_=_ G L O R Y _=_=_=_=_=_=_=_=_=_=_=_=_=_
                 -=-=-=-=-=-=-=-=-=-=-=-=-=-= A + K I L L E R =-=-=-=-=-=-=-=-=-=-=-=-=-=-
                 _______________________ A M A Z I N G  J O B ___________________________
                 ==============================================================="""

    welcome_screen = """===============================================================
        ===============================================================
        =_=_=_=_=_=_=_=_=_=_=_=_ W E L C O M E _=_=_=_=_=_=_=_=_=_=_=_=        
        _=_=_=_=_=_=_=_=_=_=_=_=_=_=_ T O _=_=_=_=_=_=_=_=_=_=_=_=_=_=_        
        -=-=-=-=-=-=-=-=-=-=-=-=-=-= T H E =-=-=-=-=-=-=-=-=-=-=-=-=-=-        
        ___________________________ G A M E ___________________________        
        ===============================================================        
        ==============================================================="""
    # just a fancy menu printer, you feed in the menu variables up above as arguments, and it will print the text. This is used at the bottom of run.py
    def print_screen(self, arg_screen): 
        for i in arg_screen:
            sys.stdout.write(i)
            sys.stdout.flush()
            time.sleep(0.008)
    # unused function for clearing the screen, might use it later.
    def clear(self):
        if name == 'nt':
            _ = system('cls')
        else:
            _ = system('clear')
    # this is the render status that actually gets called in run.py, it refers to the render status in player / enemy classes, this is so we only have to call it once, instead of twice
    def render_status(self):
        self.player_1.render_status()
        self.enemy_ai.render_status()
    # Player has his own make_choice function in his file, check it out!
    def player_take_turn(self):
        self.player_1.MakeChoice(self.enemy_ai)
    # Enemy has his own make_choice function in his file, check it out!
    def enemy_take_turn(self):
        self.enemy_ai.MakeChoice(self.player_1)
