from model.goblin import Goblin

class TestGoblin:
    """Test suite for the Goblin class"""

    def create_goblin(self):
        return Goblin(1)        

    def test_goblin_constructor(self):
        """Test that Goblin is initialized with correct attributes"""
        sample_goblin = self.create_goblin()
        assert sample_goblin._name == "Goblin 1"
        assert sample_goblin._abr == "G1"
        assert sample_goblin._hp == 10
        assert sample_goblin._dex == 8
        assert sample_goblin._speed == 5
        assert sample_goblin._melee_acc == 4
        assert sample_goblin._melee_dmg == 2
        assert sample_goblin._ranged_acc == 2
        assert sample_goblin._ranged_dmg == 1