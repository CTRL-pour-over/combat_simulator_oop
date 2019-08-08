from src import player
from src import enemy
from src.manager import Manager

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
    gm.enemy_ai.enemy_do_dmg(gm.player_1)
    gm.input_management()
    gm.render_status()

gm.game_over = True
while gm.game_over == True:
    gm.print_end_screen()
    
