from model.character import Character 
from model.creature import Creature 
from model.enemy import Enemy 

class Scenario:
    def __init__(self, character: Character, enemies: list, starting_positions: dict, num_of_positions: int):
        self._character = character
        self._enemies = enemies
        self._positions = starting_positions
        self._spaces = num_of_positions

    def damage(self, creature: Creature, dmg: int):
        hp = creature._cur_hp - dmg
        if hp <= 0:
            if isinstance(creature, Enemy):
                self.remove_enemy(creature)
            else: # Creature = character
                self.is_over() # Character loses
        else:
            creature.cur_hp(hp)

    def set_cur_hp(self, creature: Creature, hp: int):
        creature.cur_hp(hp)

    def is_over(self):
        return # TODO: end senario

    def remove_enemy(self, enemy: Enemy):
        self._enemies.remove(enemy)
        del self._positions[enemy._abr]

        # NOTE: Will need to adjust if friendly/neutral creatures are added
        if len(self._enemies) == 0:
            self.is_over() # Character wins

    def update_position(self, abr: str, new_pos: int):
        self._positions[abr] = new_pos