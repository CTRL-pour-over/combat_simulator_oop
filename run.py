from src import player
from src import enemy
from src.manager import Manager
import time
from colored import fg, bg, attr

#tree: ============ entity_class ===============
# ------ player_child -------- enemy_child -------
# ----- attk / hp --------------- attk / hp -------
# ===================================================
gm = Manager()
gm.game_start()
gm.render_status()

while gm.player_1.health > 0 and gm.enemy_ai.health > 0:
    gm.game_over = False 
    gm.enemy_threat_dmg()
    time.sleep(1)
    gm.input_management()
    time.sleep(1)
    gm.enemy_do_dmg(gm.player_1)
    time.sleep(1)
    gm.render_status()
    time.sleep(1)
gm.game_over = True
while gm.game_over == True:
    if gm.player_1.health > 0:
        gm.print_screen(gm.winner_end_screen)
    elif gm.enemy_ai.health > 0:
        gm.print_screen(gm.loser_end_screen)
    else:
        print(gm.print_screen("\nYou both fall before your knees, regret. You question whether or not the fight was worth the cause, your life. As you both bleed out, you each take a look into one anothers eyes, knowing it will be the last moment of your lives, a shared experience, none the less.\n\n"))
    
