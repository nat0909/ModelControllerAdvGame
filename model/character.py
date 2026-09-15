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

    def move(self, direction: str, spaces: int):
        """Check if the number of spaces is a valid move and spaces but + or - to match the
        direction
        
        Args:
            direction: "+" for moving right or "-" for moving left
            spaces: the number of spaces the character is trying to move 
            
        Returns: 
            If the number of spaces is greater than the character's speed (an invalid move),
            return 0
            Otherwise, return spaces and if direction is a "-", make it negative"""

        if self._speed < spaces:
            return 0

        if direction == "+":
            return spaces
        else: # direction == "-"
            return 0-spaces

