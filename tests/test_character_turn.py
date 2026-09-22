from controller.character_turn import CharacterTurn
from tests.sample_objects import SampleObjects

class TestCharacterTurn:
    def move_input(self, prompt):
        assert prompt == "Move: "
        return self.input.pop(0)

    def test_move(self): # NOTE: will need to be updated as more actions are added
        character = SampleObjects.create_character()
        self.input = ["", "-", "0", "+8"]
        space = CharacterTurn.move(character, 1, 20, self.move_input)
        assert space == 9

        self.input = ["12", "+1.2", "+1 2", "-8"]
        space = CharacterTurn.move(character, 10, 20, self.move_input)
        assert space == 2

        self.input = ["+9", "-9", "+12", "+ 2"]
        space = CharacterTurn.move(character, 1, 20, self.move_input)
        assert space == 3

        self.input = ["-6", "-5", "-4"]
        space = CharacterTurn.move(character, 5, 20, self.move_input)
        assert space == 1

        self.input = ["+6", "+5"]
        space = CharacterTurn.move(character, 15, 20, self.move_input)
        assert space == 20