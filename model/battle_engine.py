from model.creature import Creature
from model.scenario import Scenario
from model.turn_log import TurnLog
import random

class BattleEngine():
    def enemy_turn(scenario: Scenario):
        abr = scenario._character._abr
        positions = scenario._positions
        battle_log = []

        for enemy in scenario._enemies:
            old_pos = positions[enemy._abr]
            new_pos, attack = enemy.perform_turn(positions, abr)
            # implement attack logic and add to turn log
            battle_log += TurnLog(old_pos, new_pos)
        return battle_log
        
    def attack(scenario: Scenario, creature: Creature, attack_type: str, opp_dex: int):
        acc = None
        dmg = None
        if attack_type == "melee_attack":
            acc = creature._melee_acc
            dmg = creature._melee_dmg
        elif attack_type == "ranged_attack":
            acc = creature._ranged_acc
            dmg = creature._ranged_dmg

        if random.randint(0,9) + acc - opp_dex > 0: # hit
            scenario.damage(creature, dmg)

    def heal(scenario: Scenario, creature: Creature, heal: int):
        max_hp = creature._max_hp
        hp = heal + creature._cur_hp
        if hp >= max_hp:
            hp = max_hp
        scenario.set_cur_hp(hp)
