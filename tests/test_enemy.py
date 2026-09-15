from tests.sample_objects import SampleObjects

class TestEnemy():    
    def test_enemy_constructor(self):
        sample_enemy = SampleObjects.create_enemy()
        assert sample_enemy._name == "Goblin"
        assert sample_enemy._abr == "G1"
        assert sample_enemy._max_hp == 10
        assert sample_enemy._cur_hp == 10
        assert sample_enemy._dex == 5
        assert sample_enemy._speed == 3
        assert sample_enemy._melee_acc == 4
        assert sample_enemy._melee_dmg == 2
        assert sample_enemy._ranged_acc == 2
        assert sample_enemy._ranged_dmg == 2

    def test_move_towards(self):
        sample_enemy = SampleObjects.create_enemy()
        assert sample_enemy.move_towards({"FU": 5, "G1": 7}, "FU", 10) == 6 # Test basic movement
        assert sample_enemy.move_towards({"FU": 5, "G1": 6}, "FU", 10) == 6 # Test can stay in same position
        assert sample_enemy.move_towards({"FU": 5, "G1": 7, "G2": 6,}, "FU", 10) == 4 # Test movement around target
        assert sample_enemy.move_towards({"FU": 5, "G1": 10}, "FU", 10) == 7 # Test movement towards but not reaching target
        assert sample_enemy.move_towards({"FU": 5, "G1": 2, "G2": 3, "G3": 4,}, "FU", 10) == 2 # Test cannot move closer
        assert sample_enemy.move_towards({"FU": 1, "G1": 3, "G2": 2}, "FU", 10) == 3 # Test lower bound
        assert sample_enemy.move_towards({"FU": 10, "G1": 8, "G2": 9}, "FU", 10) == 8 # Test upper bound