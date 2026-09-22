from model.creature import Creature

class Character(Creature):
    def __init__(self, name: str, character_class: str, max_hit_points: int, dexterity: int, speed: int, melee_accuracy: int, melee_damage: int, ranged_accuracy: int, ranged_damage: int):
        super().__init__(
            name, 
            name[0:2].upper(), # abreviation
            max_hit_points, 
            dexterity, 
            speed,
            melee_accuracy, 
            melee_damage, 
            ranged_accuracy, 
            ranged_damage
        )
        self._char_class = character_class

    def set_class(self, char_class):
        self._char_class = char_class

