from controller.scenario_controller import ScenarioController

class FakeScenario:
    def __init__(self, spaces, positions):
        self._spaces = spaces
        self._positions = positions

class TestScenarioController:
    def test_display_board(self):
        scenario = FakeScenario(5, {"MI": 1, "G1": 3})
        assert ScenarioController.display_board(scenario) == "MI __ G1 __ __ "
        scenario = FakeScenario(3, {})
        assert ScenarioController.display_board(scenario) == "__ __ __ "
        scenario = FakeScenario(4, {"MI": 2, "G1": 3})
        assert ScenarioController.display_board(scenario) == "__ MI G1 __ "
