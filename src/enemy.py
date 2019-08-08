from src.entity import entity
from colored import fg

class enemy_child(entity):
    name = "Enemy"
    public  = 150

    def takes_his_turn(self):
        pass

    def enemy_do_dmg(self, argument):
        print("%s Enemy about to inflict " % (fg(1)), enemy_child.damage, "%s Type damage on your ass." % (fg(1)))
        argument.health = argument.health - enemy_child.damage

    def enemy_deflect_incoming_dmg(self, argument):
        print("%s Enemy deflecting " % (fg(1)), argument.defense)
        argument.damage = argument.damage - enemy_child.defense
        print("%s Enemy taking " % (fg(1)), argument.damage)
        enemy_child.health = enemy_child.health - argument.damage
        print("%s Enemy hp: " % (fg(1)), enemy_child.health)
