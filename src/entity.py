from colored import fg
import random

class entity(object):

# instantiate the entity object
    def __init__(self, arg_color = "%s" % fg(11), arg_name = "Default Entity", arg_health = 100, arg_damage = random.randrange(1, 100), arg_defense = random.randrange(1, 100)):
        self.color = arg_color
        self.name = arg_name
        self.health = arg_health
        self.damage = arg_damage
        self.defense = arg_defense
# render all stats   
    def render_status(self):
        print(self.color)
        print("\n\nName: ", self.name)        
        print("Health: ", self.health) 
        print("Damage: ", self.damage) 
        print("Defense: ", self.defense) 
# this function gets overrided in both player / enemy classes
    def MakeChoice(self):
        print("""%s\n\t\t\tOPTIONS:
                                1: ----Attack-----
                                2: ----Defend-----
                                3: ----Roll For Damage Buff----
                                4: ----Roll For Defense Buff----
                                5: ----Eat An Apple----
                                """ % fg(117))

# changes damage stat to a number 1 - 100
    def roll_for_damage(self, arg_entity):
        arg_entity.damage = random.randrange(1, 100)
        print('\n', arg_entity.color, arg_entity.name, "rolls for a new Damage Stat: ", arg_entity.damage)
# changes defense stat to a number 1 - 100
    def roll_for_defense(self, arg_entity):
        arg_entity.defense = random.randrange(1, 100)
        print('\n', arg_entity.color, arg_entity.name, "rolls for a new Defense Stat: ", arg_entity.defense)
# adds value to entity health, gives -50 -- 200 health to an entity.
    def eat_apple(self, arg_entity):
        calculated_health_buff = random.randrange(-50, 200)
        print(arg_entity.color, "\nWow! That apple gave", arg_entity.name,  calculated_health_buff, "hp! That's crazy!")
        print('UwU, that was so tasty!', arg_entity.name, 'Current hp:', arg_entity.health, "+ hp from apple:", calculated_health_buff, "hp")
        arg_entity.health = calculated_health_buff + arg_entity.health
        print(arg_entity.name, "now has: ", arg_entity.health, "hp. Good luck next round!!")
# BROKEN DEFEND_INCOMING_ATTK FUNCTION, PLAYER & ENEMY DO NOT GIVE EACH OTHER THE REQUIRED STATS AT RUN TIME IN ORDER TO MAKE THIS WORK
    def defend_incoming_attack(self, arg_entity):
        print("\n", arg_entity.color, arg_entity.name, "deflecting", arg_entity.defense, "Incoming damage")
        calculated_damage_done = arg_entity.damage - arg_entity.defense
        print(arg_entity.name, "taking ", calculated_damage_done, "damage")
        arg_entity.health = arg_entity.health - calculated_damage_done
        print(arg_entity.name, ": ", arg_entity.health, "current health")
# Deals damage to entity
    def violate_opponent(self, arg_player, arg_enemy):
        arg_enemy.health = arg_enemy.health - arg_player.damage
        print(arg_player.color, "\n", arg_player.name ," pounces on the enemy, dealing", arg_player.damage, "damage. Leaving the enemy with", arg_enemy.health, "hp...", arg_player.name, ", you are determined.")
