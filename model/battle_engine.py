from model.creature import Creature
from model.scenario import Scenario
from model.turn_log import TurnLog
import random

class BattleEngine():
    @staticmethod
    def enemy_turn(scenario: Scenario):
        char_abr = scenario._character._abr
        char_dex = scenario._character._dex
        positions = scenario._positions
        battle_log = []

        
        for enemy in scenario._enemies:
            old_pos = positions[enemy._abr]
            new_pos, attack_type = enemy.perform_turn(positions, char_abr)
            hit, dmg = BattleEngine.attack(scenario, enemy, attack_type, char_dex)
                        
            log = TurnLog(enemy._name, old_pos, new_pos, hit, dmg)
            battle_log.append(log)
        return battle_log

    @staticmethod
    def attack(scenario: Scenario, creature: Creature, attack_type: str, opp_dex: int):
        acc = 0
        dmg = 0
        if attack_type == "melee_attack":
            acc = creature._melee_acc
            dmg = creature._melee_dmg
        elif attack_type == "ranged_attack":
            acc = creature._ranged_acc
            dmg = creature._ranged_dmg

        if random.randint(0,9) + acc - opp_dex > 0: # hit
            scenario.damage(creature, dmg)
            return True, dmg
        else:
            return False, -1

    @staticmethod
    def heal(scenario: Scenario, creature: Creature, heal: int):
        max_hp = creature._max_hp
        hp = heal + creature._cur_hp
        if hp >= max_hp:
            hp = max_hp
        scenario.set_cur_hp(creature, hp)
