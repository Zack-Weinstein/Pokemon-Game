#what calculations do I need to get?
#1 Attack Damage based on the type of pokemon and multipliers
#2 Damage taken by the pokemon attacked
## trigger something if the pokemon is at 0 HP


#how to calculate the modifier???
#if attacking pokemon type is ___ and defending pokemon is ___use multipliers 
level = 50 #placeholder
attack_def_ratio = (a/d)
damage = ((((((2*level)/5)+2)* power)* attack_def_ratio)/50)* modifier

Modifier = Critical × Random × Type


def calculate_damage(self, currentMove, attacker): #self can be the computer and player
    #c.calculate_damage-- outputs damge #c is self #c is also pokemon class
    #damage dealt to other pokemon
    #Zack is doing (HP- calculate_damage)
    ###
    damage = 10
    return damage
    '''Calculates the damage taken from an attack'''
    