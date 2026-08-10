from model.enemy import Enemy

class TestEnemy():
    """Test suite for the class Enemy"""

    def create_enemy():
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
        """Test that Enemy is initialized with correct attributes"""
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

    def test_move_towards(self,):
        positions = []

        Enemy.move_towards(positions, index)