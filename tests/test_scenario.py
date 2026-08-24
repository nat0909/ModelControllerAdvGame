from model.character import Character
from model.enemy import Enemy
from model.scenario import Scenario

class TestScenario:
    def create_character(self):
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

    def create_enemy(self, abr="G1", hp=10):
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

    def create_scenario(self, enemies=None, positions=None):
        character = self.create_character()
        enemies = enemies if enemies is not None else [self.create_enemy()]
        if positions is None:
            positions = {"MI": 0, "G1": 3}
        scenario = Scenario(character, enemies, positions, 100)
        return scenario, character, enemies

    def test_constructor(self):
        scenario, character, enemies = self.create_scenario()
        assert scenario._character == character
        assert scenario._enemies == enemies
        assert scenario._positions == {"MI": 0, "G1": 3}

    def test_damage_reduces_hp_without_defeat(self):
        scenario, _, enemies = self.create_scenario()
        enemy = enemies[0]
        scenario.damage(enemy, 4)
        assert enemy._cur_hp == 6
        assert enemy in scenario._enemies

    def test_damage_removes_enemy_when_hp_drops_to_zero(self):
        scenario, _, enemies = self.create_scenario()
        enemy = enemies[0]
        scenario.damage(enemy, 10)
        assert enemy not in scenario._enemies
        assert "G1" not in scenario._positions

    def test_damage_removes_enemy_when_hp_drops_below_zero(self):
        scenario, _, enemies = self.create_scenario()
        enemy = enemies[0]
        scenario.damage(enemy, 15)
        assert enemy not in scenario._enemies

    def test_damage_ends_scenario_when_character_defeated(self, monkeypatch):
        scenario, character, _ = self.create_scenario()
        called = []
        monkeypatch.setattr(scenario, "is_over", lambda: called.append(True))
        scenario.damage(character, 20)
        assert called == [True]

    def test_set_cur_hp(self):
        scenario, _, enemies = self.create_scenario()
        enemy = enemies[0]
        scenario.damage(enemy, 4)
        scenario.set_cur_hp(enemy, 9)
        assert enemy._cur_hp == 9

    def test_remove_enemy(self):
        scenario, _, enemies = self.create_scenario()
        enemy = enemies[0]
        scenario.remove_enemy(enemy)
        assert enemy not in scenario._enemies
        assert "G1" not in scenario._positions

    def test_remove_last_enemy_ends_scenario(self, monkeypatch):
        scenario, _, enemies = self.create_scenario()
        called = []
        monkeypatch.setattr(scenario, "is_over", lambda: called.append(True))
        scenario.remove_enemy(enemies[0])
        assert called == [True]

    def test_remove_enemy_does_not_end_scenario_when_others_remain(self, monkeypatch):
        enemy1 = self.create_enemy(abr="G1")
        enemy2 = self.create_enemy(abr="G2")
        scenario, _, _ = self.create_scenario(
            enemies=[enemy1, enemy2],
            positions={"MI": 0, "G1": 3, "G2": 5},
        )
        called = []
        monkeypatch.setattr(scenario, "is_over", lambda: called.append(True))
        scenario.remove_enemy(enemy1)
        assert called == []
        assert scenario._enemies == [enemy2]

    def test_update_position(self):
        scenario, _, _ = self.create_scenario()
        scenario.update_position("G1", 7)
        assert scenario._positions["G1"] == 7

    def test_is_over_returns_none(self):
        scenario, _, _ = self.create_scenario()
        assert scenario.is_over() is None
