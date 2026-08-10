from model.character import Character
from model.goblin import Goblin
import random

class BattleEngine():
    def battle(positions: list, enemies: list, character: Character):
        return # TODO

    def attack(acc: int, dmg: int, opp_dex: int):
        if random.randint(0,9) + acc - opp_dex > 0: # hit
            return dmg
        return 0 # miss

    def heal(max_hp, cur_hp, heal):
        hp = heal + cur_hp
        if hp >= max_hp:
            return max_hp
        return hp
