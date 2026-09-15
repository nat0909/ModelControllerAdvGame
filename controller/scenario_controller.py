from model.scenario import Scenario
from model.battle_engine import BattleEngine
from model.turn_log import TurnLog

class ScenarioController:
    @staticmethod
    def start_scenario(scenario: Scenario):
        is_over = False
        while not is_over:
            ScenarioController.char_turn(scenario) # TODO
            log = BattleEngine.enemy_turn(scenario)
            for turn in log:
                print(ScenarioController.display_turn(turn))
            # print state, take player input, etc.

    @staticmethod
    def char_turn(scenario: Scenario): # TODO
        return

    @staticmethod
    def display_board(scenario: Scenario):
        occupants = {}
        for abr, pos in scenario._positions.items():
            occupants[pos] = abr

        board = ""
        for space in range(1, scenario._spaces + 1):
            board += occupants.get(space, "__")
            board += " "
        return board

    @staticmethod
    def display_turn(turn_log: TurnLog):
        return