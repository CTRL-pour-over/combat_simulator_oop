from src.entity import entity
from colored import fg

class player_child(entity):
    # default values for player, these values get over-written in Manager
    def __init__(self, arg_color = "%s" % fg(2), arg_name = "Default Player", arg_health = 100, arg_damage = 50, arg_defense = 50):
        self.color = arg_color
        self.name = arg_name
        self.health = arg_health
        self.damage = arg_damage
        self.defense = arg_defense
    # prints players stats to screen, gets called in the managers render_status
    def render_status(self):
        print(self.color)
        print("\nName: ", self.name)        
        print("Health: ", self.health) 
        print("Damage: ", self.damage) 
        print("Defense: ", self.defense) 
    # option menu for the player, this gets called in the Managers "player_take_turn" function. cool right?
    def MakeChoice(self, arg_enemy):
        super(player_child)
        try:
            option_select = int(input("""%s\n\t\t\tOPTIONS:
                                1: ----Attack-----
                                2: ----Defend-----
                                3: ----Roll For Damage Buff----
                                4: ----Roll For Defense Buff----
                                5: ----Eat An Apple----
                                Choose: >>>  """ % fg(117)))
            if option_select == 1:
                self.violate_opponent(self, arg_enemy)
            elif option_select == 2:
                self.defend_incoming_attack(self)
            elif option_select == 3:
                self.roll_for_damage(self)
            elif option_select == 4:
                self.roll_for_defense(self)
            elif option_select == 5:
                self.eat_apple(self)
            else:
                print("You fumble before your enemy. What a disgrace.")
                self.health = self.health - 50
                print("-50 hp")
        except ValueError:
            print("\nOops! That was not a valid number. s o r r y . . .      T_T\n")
