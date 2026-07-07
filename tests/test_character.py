from model.character import Character

class TestGoblin:
    """Test suite for the Character class"""

    def create_character(self):
        return Character(
            "Mivari",
            20,
            6,
            4,
            3,
            10,
            5)        

    def test_character_constructor(self):
        """Test that Character is initialized with correct attributes"""
        sample_creature = self.create_character()
        assert sample_creature._name == "Mivari"
        assert sample_creature._abr == "MI"
        assert sample_creature._hp == 20
        assert sample_creature._dex == 6
        assert sample_creature._melee_acc == 4
        assert sample_creature._melee_dmg == 3
        assert sample_creature._ranged_acc == 10
        assert sample_creature._ranged_dmg == 5