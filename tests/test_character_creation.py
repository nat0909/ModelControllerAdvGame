from controller.character_creation import CharacterCreation

class TestCharacterCreation():
    """Test suite for the CharacterCreation class"""
    
    def test_determine_stats(self):
        max_hp, dex, speed, melee_acc, melee_dmg, ranged_acc, ranged_dmg = CharacterCreation.determine_stats("warrior")
        assert max_hp == 30
        assert dex == 4
        assert speed == 3
        assert melee_acc == 6
        assert melee_dmg == 4
        assert ranged_acc == 2
        assert ranged_dmg == 2
        max_hp, dex, speed, melee_acc, melee_dmg, ranged_acc, ranged_dmg = CharacterCreation.determine_stats("ranger")
        assert max_hp == 20
        assert dex == 2
        assert speed == 8
        assert melee_acc == 2
        assert melee_dmg == 2
        assert ranged_acc == 6
        assert ranged_dmg == 4
        max_hp, dex, speed, melee_acc, melee_dmg, ranged_acc, ranged_dmg = CharacterCreation.determine_stats("rogue")
        assert max_hp == 20
        assert dex == 6
        assert speed == 6
        assert melee_acc == 6
        assert melee_dmg == 2
        assert ranged_acc == 6
        assert ranged_dmg == 2

    def name_input(self, prompt):
        assert prompt == "Name: "
        return self.inputs.pop(0)

    def test_choose_name(self):
        self.inputs = ["m1vari", "m!vari", "miv ari", "     mivaRi  "]
        assert CharacterCreation.choose_name(user_input=self.name_input) == "Mivari"

    def class_input(self, prompt):
        assert prompt == "Class: "
        return self.inputs.pop(0)
    
    def test_choose_class(self):
        self.inputs = ["warrior", "1"]
        assert CharacterCreation.choose_class(user_input=self.class_input) == "warrior"
        self.inputs = ["5", "  2 "]
        assert CharacterCreation.choose_class(user_input=self.class_input) == "ranger"
        self.inputs = ["3a", "3"]
        assert CharacterCreation.choose_class(user_input=self.class_input) == "rogue"