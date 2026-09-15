from controller.character_turn import CharacterTurn
from tests.sample_objects import SampleObjects

class TestCharacterTurn:
    def option_input(self, prompt):
        assert prompt == "Option:"
        #return self.input.pop(0)

    def test_prompt_player(self): # NOTE: will need to be updated as more actions are added
        scenario, _, _ = SampleObjects.create_scenario()
        self.input = {"0", "", "Move", "1"}
        CharacterTurn.prompt_player(scenario, False, TestCharacterTurn.option_input)
        # TODO