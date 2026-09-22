# from model.character import Character
from model.scenario import Scenario
from model.character import Character
from model.turn_log import TurnLog

class CharacterTurn:
    @staticmethod
    def prompt_player(scenario: Scenario, tutorial: bool = False, user_input=input):
        char = scenario._character
        abr = char._abr
        old_space = scenario._positions[abr]
        new_space = old_space

        if tutorial: # TODO: finish implementing tutorial
            print("You have 2 actions per turn.")
            print("Moving and attacking both count as actions.")
            print("TODO")

        print("\nType the number of the option you want.")
        print("1. Move")
        # TODO: implement other actions, including attack

        while True:
            option = user_input("Option: ").strip()
            if option == "1":
                new_space = CharacterTurn.move(char, old_space, scenario._spaces, user_input)
                scenario.update_position(abr, new_space)
                break
            else:
                print("\nInvalid input. Type the number cooresponding with the option you want.")

        log = TurnLog(char._name, old_space, new_space)
        return log

    @staticmethod
    def move(char: Character, cur_space : int, max_spaces: int, user_input=input) -> int:
        print(f"\nYou are currently on space {cur_space}.")
        print("Type the direction (+/-) and number of spaces you want to move.")
        new_space = cur_space

        while True:
            movement = user_input("Move: ").strip()
            if len(movement) >= 2:
                direction = movement[:1]
                spaces = movement[1:].strip()

                if (direction == "+" or direction == "-") and spaces.isdigit():
                    spaces = int(spaces)
                    speed = char._speed

                    # Find the space the player wants to move to
                    chosen_space = new_space
                    if direction == "+":
                        chosen_space += spaces
                    else: # direction == "-"
                        chosen_space -= spaces

                    # Checks if its an invalid move, if not: break
                    if spaces == 0:
                        print("\nInvalid move. You must move at least 1 space.")
                        continue
                    elif speed < spaces:
                        print(f"\nInvalid move. You cannot move more than {speed} spaces.")
                        continue
                    elif chosen_space < 1 or chosen_space > max_spaces:
                        print(f"\nInvalid move: out of bounds. You must stay between spaces 1 to {max_spaces}.")
                        continue
                    else:
                        new_space = chosen_space
                        break

            # Error message for if it was an invalid input, NOT invalid move
            print("\nInvalid input. Type the direction (+/-) and the number of spaces you want to move.")

        print(f"\nYou moved to space {new_space}.")
        return new_space

        

        
        
