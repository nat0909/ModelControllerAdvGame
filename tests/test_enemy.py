from model.enemy import Enemy

class TestEnemy():
    def create_enemy(self):
        return Enemy(
            "Goblin",
            "G1",
            10,
            5,
            3,
            4,
            2,
            2,
            2,
        )
    
    def test_enemy_constructor(self):
        sample_enemy = self.create_enemy()
        assert sample_enemy._name == "Goblin"
        assert sample_enemy._abr == "G1"
        assert sample_enemy._hp == 10
        assert sample_enemy._dex == 5
        assert sample_enemy._speed == 3
        assert sample_enemy._melee_acc == 4
        assert sample_enemy._melee_dmg == 2
        assert sample_enemy._ranged_acc == 2
        assert sample_enemy._ranged_dmg == 2

    def test_move_towards(self):
        sample_enemy = self.create_enemy()
        assert sample_enemy.move_towards({"FU": 0, "G1": 2}, "FU") == 1
        assert sample_enemy.move_towards({"FU": 0, "G1": 1}, "FU") == 1
        assert sample_enemy.move_towards({"FU": 0, "G1": -2}, "FU") == -1
        assert sample_enemy.move_towards({"FU": 0, "G1": 2, "G2": 1}, "FU") == -1
        assert sample_enemy.move_towards({"FU": 0, "G1": 10}, "FU") == 7
        assert sample_enemy.move_towards({"FU": 0, "G1": 3, "G2": 2, "G3": 1}, "FU") == 3