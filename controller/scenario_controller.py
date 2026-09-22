from controller.character_turn import CharacterTurn
from controller.formatting import Formatting
from model.scenario import Scenario
from model.battle_engine import BattleEngine
from model.turn_log import TurnLog
import time

class ScenarioController:
    @staticmethod
    def run_scenario(scenario: Scenario):
        is_over = False
        while not is_over:
            Formatting.section_title("Your Turn")
            log = CharacterTurn.prompt_player(scenario)
            print(ScenarioController.display_board(scenario))
            time.sleep(2)

            Formatting.section_title("Enemy Turns")
            log = BattleEngine.enemy_turn(scenario)
            for turn in log:
                print(ScenarioController.display_turn(turn))
                print(ScenarioController.display_board(scenario))
                time.sleep(2)

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
        name = turn_log._name
        old_pos = turn_log._old_position
        new_pos = turn_log._new_position

        print_log = f"\n{name}'s turn: \n"
        if old_pos != new_pos:
            print_log += f"{name} moved to {new_pos}."

        return print_log
