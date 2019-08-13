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
    gm.enemy_do_dmg(gm.player_1)
    time.sleep(1)
    gm.input_management()
    time.sleep(1)
    gm.render_status()
    time.sleep(1)
gm.game_over = True
while gm.game_over == True:
    gm.print_end_screen()
    
