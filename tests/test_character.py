from model.character import Character

class TestCharacter:
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
            5)        

    def test_character_constructor(self):
        sample_character = self.create_character()
        assert sample_character._name == "Mivari"
        assert sample_character._abr == "MI"
        assert sample_character._char_class == "rogue"
        assert sample_character._hp == 20
        assert sample_character._dex == 6
        assert sample_character._speed == 8
        assert sample_character._melee_acc == 4
        assert sample_character._melee_dmg == 3
        assert sample_character._ranged_acc == 10
        assert sample_character._ranged_dmg == 5

    def test_set_class(self):
        sample_character = self.create_character()
        sample_character.set_class("warrior")
        assert sample_character._char_class == "warrior"
