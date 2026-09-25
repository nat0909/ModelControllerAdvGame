# from model.character import Character
from controller.formatting import Formatting
from model.scenario import Scenario
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

        actions_remaining = 2
        list_options = True
        while actions_remaining > 0:
            if list_options:
                print("Type the number of the option you want.")
                print("1. Move")
                print("2. Melee Attack")            
            option = user_input("Option: ").strip()
            if option == "1":
                new_space = CharacterTurn.move(scenario, user_input)
                scenario.update_position(abr, new_space)
                actions_remaining -= 1
                list_options = True
            elif option == "2":
                CharacterTurn.melee_attack(scenario, user_input)
                actions_remaining -= 1
                list_options = True
            else:
                print("\nInvalid input. Type the number cooresponding with the option you want.")
                list_options = False

        log = TurnLog(char._name, old_space, new_space)
        return log

    @staticmethod
    def melee_attack(scenario: Scenario, user_input=input): # TODO: implement actual attacking
        char = scenario._character
        cur_space = scenario._positions[char._abr]
        enemies = scenario._enemies
        positions = scenario._positions

        print(f"\nYou are currently on space {cur_space}:")
        print(Formatting.display_board(scenario))
        print("\nType the number of the enemy you would like to attack.")
        num = 1
        nums = []
        for enemy in enemies:
            print(f"{num}. {enemy._name} ({enemy._abr})")
            nums.append(num)
            num += 1

        while True:
            choice = user_input("Enemy: ").strip()
            for n in nums:
                if choice == f"{n}":
                    enemy = enemies[n-1]
                    print(f"\nYou attack {enemy._name}.\n")
                    return
            print("\nInvalid input. Type the number cooresponding with the enemy you want.")

    @staticmethod
    def move(scenario: Scenario, user_input=input) -> int:
        char = scenario._character
        cur_space = scenario._positions[char._abr]
        max_spaces = scenario._spaces

        print(f"\nYou are currently on space {cur_space}:")
        print(Formatting.display_board(scenario))
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
                    positions = scenario._positions.values()
                    is_taken = False

                    # Find the space the player wants to move to
                    chosen_space = new_space
                    if direction == "+":
                        chosen_space += spaces
                    else: # direction == "-"
                        chosen_space -= spaces

                    # Checks if its an invalid move, if not: break
                    for position in positions: # Checks if any creatures occupies the space
                        if position == chosen_space:
                            is_taken = True
                    if spaces == 0: # If they aren't moving
                        print("\nInvalid move. You must move at least 1 space.")
                        continue
                    elif speed < spaces: # If they are moving more spaces than their speed
                        print(f"\nInvalid move. You cannot move more than {speed} spaces.")
                        continue
                    elif chosen_space < 1 or chosen_space > max_spaces: # If they are going out of bounds
                        print(f"\nInvalid move: out of bounds. You must stay between spaces 1 to {max_spaces}.")
                        continue
                    elif is_taken: # If another creature occupies the space
                        print("\nInvalid move. Another creature is on this space.")
                    else: # Otherwise if it works                   
                        new_space = chosen_space
                        break

            # Error message for if it was an invalid input, NOT invalid move
            print("\nInvalid input. Type the direction (+/-) and the number of spaces you want to move.")

        print(f"\nYou moved to space {new_space}.")
        return new_space

        

        
        
