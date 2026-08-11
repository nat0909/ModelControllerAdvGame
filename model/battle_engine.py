from model.character import Character
from model.creature import Creature
from model.enemy import Enemy
from model.scenario import Scenario
import random

class BattleEngine():
    def battle(scenario: Scenario):
        while True:
            scenario._char.perform_turn()
            abr = scenario._char._abr
            for enemy in scenario._enemies:
                enemy.perform_turn(scenario._positions, abr)
        
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
