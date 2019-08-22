from src import player
from src import enemy
from src.manager import Manager
import time
from colored import fg, bg, attr

###########ORIGINAL_DESIGN_ARCHITECTURE##############
#tree: ============ entity_class ====================
# ------ player_child -------- enemy_child ----------
# ----- attk / hp --------------- attk / hp ---------
# ===================================================

# renaming the manager class
gm = Manager()
# printing welcome screen
gm.print_screen(gm.welcome_screen)
#vVvVvVvVvVv MAIN GAME LOOP, GAME IS RUN HERE vVvVvVvV##
### gm.render_status, gm.player_take_turn, gm.enemy_take_turn are functions that live in Manager. ###
while gm.player_1.health > 0 and gm.enemy_ai.health > 0:
    gm.game_over = False 

    gm.render_status()
    time.sleep(1)
    gm.player_take_turn()
    time.sleep(2)
    gm.enemy_take_turn()
    time.sleep(2)
gm.game_over = True

# game over logic, just figures out which loading screen to play   #
# everything that starts with gm is coming from the Manager class. #
while gm.game_over == True:
    if gm.player_1.health > 0:
        gm.print_screen(gm.winner_end_screen)
    elif gm.enemy_ai.health > 0:
        gm.print_screen(gm.loser_end_screen)
    else:
        print(gm.print_screen("\nYou both fall before your knees, regret. You question whether or not the fight was worth the cause, your life. As you both bleed out, you each take a look into one anothers eyes, knowing it will be the last moment of your lives, a shared experience, none the less.\n\n"))
