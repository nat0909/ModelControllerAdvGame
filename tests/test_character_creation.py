from controller.character_creation_controller import CharacterCreation

class TestCharacterCreation():
    """Test suite for the CharacterCreation class"""

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