from controller.character_creation import CharacterCreation

class TestCharacterCreation():
    def character_input(self, prompt):
        assert prompt == "Name: " or "Class: "
        return self.inputs.pop(0)

    def test_create_character(self):
        self.inputs = ["mivari", "1"]
        char = CharacterCreation.create_character(self.character_input)
        assert char._max_hp == 30
        assert char._dex == 8
        assert char._speed == 4
        assert char._melee_acc == 6
        assert char._melee_dmg == 4
        assert char._ranged_acc == 2
        assert char._ranged_dmg == 2

        self.inputs = ["mivari", "2"]
        char = CharacterCreation.create_character(self.character_input)
        assert char._max_hp == 20
        assert char._dex == 6
        assert char._speed == 8
        assert char._melee_acc == 2
        assert char._melee_dmg == 2
        assert char._ranged_acc == 6
        assert char._ranged_dmg == 4

        self.inputs = ["mivari", "3"]
        char = CharacterCreation.create_character(self.character_input)
        assert char._max_hp == 20
        assert char._dex == 10
        assert char._speed == 6
        assert char._melee_acc == 6
        assert char._melee_dmg == 2
        assert char._ranged_acc == 6
        assert char._ranged_dmg == 2

    def test_determine_stats(self):
        max_hp, dex, speed, melee_acc, melee_dmg, ranged_acc, ranged_dmg = CharacterCreation.determine_stats("warrior")
        assert max_hp == 30
        assert dex == 8
        assert speed == 4
        assert melee_acc == 6
        assert melee_dmg == 4
        assert ranged_acc == 2
        assert ranged_dmg == 2

        max_hp, dex, speed, melee_acc, melee_dmg, ranged_acc, ranged_dmg = CharacterCreation.determine_stats("ranger")
        assert max_hp == 20
        assert dex == 6
        assert speed == 8
        assert melee_acc == 2
        assert melee_dmg == 2
        assert ranged_acc == 6
        assert ranged_dmg == 4
        
        max_hp, dex, speed, melee_acc, melee_dmg, ranged_acc, ranged_dmg = CharacterCreation.determine_stats("rogue")
        assert max_hp == 20
        assert dex == 10
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
    