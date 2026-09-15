from model.character import Character
from model.enemy import Enemy
from model.scenario import Scenario

class SampleObjects:
    @staticmethod
    def create_character():
        return Character(
            "Mivari",
            "rogue",
            20,
            6,
            8,
            4,
            3,
            10,
            5,
        )

    @staticmethod
    def create_enemy(abr="G1", hp=10):
        return Enemy(
            "Goblin",
            abr,
            hp,
            5,
            3,
            4,
            2,
            2,
            2,
        )

    @staticmethod
    def create_scenario(enemies=None, positions=None, spaces=5):
        character = SampleObjects.create_character()
        enemies = enemies if enemies is not None else [SampleObjects.create_enemy()]
        if positions is None:
            positions = {"MI": 1, "G1": 3}
        scenario = Scenario(character, enemies, positions, spaces)
        return scenario, character, enemies