from model.goblin import Goblin

class TestGoblin:
    """Test suite for the Goblin class"""

    def create_goblin(self):
        return Goblin(1)        

    def test_goblin_constructor(self):
        """Test that Goblin is initialized with correct attributes"""
        sample_creature = self.create_goblin()
        assert sample_creature._name == "Goblin 1"
        assert sample_creature._abr == "G1"
        assert sample_creature._hp == 10
        assert sample_creature._dex == 5
        assert sample_creature._melee_acc == 4
        assert sample_creature._melee_dmg == 2
        assert sample_creature._ranged_acc == 2
        assert sample_creature._ranged_dmg == 2