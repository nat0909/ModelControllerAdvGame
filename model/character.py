from creature import Creature

class Character(Creature):
    def __init__(self, name: str, max_hit_points: int, dexterity: int, melee_accuracy: int, melee_damage: int, ranged_accuracy: int, ranged_damage: int):
        super().__init__(
            name, 
            name[0:2].upper(), # abreviation
            max_hit_points, 
            dexterity, 
            melee_accuracy, 
            melee_damage, 
            ranged_accuracy, 
            ranged_damage
        )
