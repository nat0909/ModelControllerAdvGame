from model.scenario import Scenario
from model.battle_engine import BattleEngine

class ScenarioController:
    def start_scenario(scenario: Scenario):
        is_over = False
        while not is_over:
            ScenarioController.char_turn()
            BattleEngine.enemy_turns(scenario)
            # print state, take player input, etc.

    def char_turn(scenario: Scenario):
        return

    def display_board(scenario: Scenario):
        board = ""
        for space in range(scenario._spaces):
            occupied = False
            for abr, occupied_space in scenario._positions.items():
                if occupied_space == space:
                    board += abr
                    occupied = True
            if not occupied:
                board += "__"
        return board