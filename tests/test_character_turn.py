from controller.character_turn import CharacterTurn
from tests.sample_objects import SampleObjects

class TestCharacterTurn:
    def move_input(self, prompt):
        assert prompt == "Move: "
        return self.input.pop(0)

    def test_move(self): # NOTE: will need to be updated as more actions are added
        scenario1, _, _ = SampleObjects.create_scenario(None, None, 20)
        scenario2, _, _ = SampleObjects.create_scenario(None, {"MI": 5, "G1": 3}, 20)
        scenario3, _, _ = SampleObjects.create_scenario(None, {"MI": 10, "G1": 3}, 20)
        scenario4, _, _ = SampleObjects.create_scenario(None, {"MI": 15, "G1": 3}, 20)

        self.input = ["", "-", "0", "+8"]
        space = CharacterTurn.move(scenario1, self.move_input)
        assert space == 9

        self.input = ["12", "+1.2", "+1 2", "-8"]
        space = CharacterTurn.move(scenario3, self.move_input)
        assert space == 2

        self.input = ["+9", "-9", "+12", "+ 3"]
        space = CharacterTurn.move(scenario1, self.move_input)
        assert space == 4

        self.input = ["-6", "-5", "-4"]
        space = CharacterTurn.move(scenario2, self.move_input)
        assert space == 1

        self.input = ["+6", "+5"]
        space = CharacterTurn.move(scenario4, self.move_input)
        assert space == 20

        self.input = ["+2", "+4"]
        space = CharacterTurn.move(scenario1, self.move_input)
        assert space == 5