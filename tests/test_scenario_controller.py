from controller.scenario_controller import ScenarioController
from tests.sample_objects import SampleObjects

class TestScenarioController:
    def test_display_board(self):
        scenario, _, _ = SampleObjects.create_scenario()
        assert ScenarioController.display_board(scenario) == "MI __ G1 __ __ "
        scenario, _, _ = SampleObjects.create_scenario(None, {}, 3)
        assert ScenarioController.display_board(scenario) == "__ __ __ "
        scenario, _, _ = SampleObjects.create_scenario(None, {"MI": 2, "G1": 3}, 4)
        assert ScenarioController.display_board(scenario) == "__ MI G1 __ "
