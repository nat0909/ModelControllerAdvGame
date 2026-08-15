from controller.scenario_controller import ScenarioController

class FakeScenario:
    def __init__(self, spaces, positions):
        self._spaces = spaces
        self._positions = positions

class TestScenarioController:

    def test_display_board_marks_occupied_spaces(self):
        scenario = FakeScenario(6, {"MI": 0, "G1": 3})
        assert ScenarioController.display_board(scenario) == "MI____G1____"

    def test_display_board_all_empty(self):
        scenario = FakeScenario(3, {})
        assert ScenarioController.display_board(scenario) == "______"

    def test_display_board_adjacent_occupants(self):
        scenario = FakeScenario(4, {"MI": 1, "G1": 2})
        assert ScenarioController.display_board(scenario) == "__MIG1__"

    def test_display_board_multiple_occupants_same_space(self):
        scenario = FakeScenario(2, {"MI": 0, "G1": 0})
        assert ScenarioController.display_board(scenario) == "MIG1__"
