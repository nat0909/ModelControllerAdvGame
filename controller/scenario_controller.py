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
        print(ScenarioController.scenario_start(scenario))
        time.sleep(2)
        while not is_over:
            print(Formatting.section_sub_title("Your Turn"))
            log = CharacterTurn.prompt_player(scenario)
            print(Formatting.display_board(scenario))
            time.sleep(2)

            print(Formatting.section_sub_title("Enemy Turns"))
            log = BattleEngine.enemy_turn(scenario)
            for turn in log:
                print(ScenarioController.display_turn(turn))
                print(Formatting.display_board(scenario))
                time.sleep(2)

    @staticmethod
    def scenario_start(scenario: Scenario) -> str:
        text = Formatting.section_title("SCENARIO START")
        text += "Board:\n"
        text += Formatting.display_board(scenario)
        return text     
    
    @staticmethod
    def display_turn(turn_log: TurnLog) -> str:
        name = turn_log._name
        old_pos = turn_log._old_position
        new_pos = turn_log._new_position

        print_log = f"{name}'s turn: \n"
        if old_pos != new_pos:
            print_log += f"{name} moved to {new_pos}."

        return print_log
