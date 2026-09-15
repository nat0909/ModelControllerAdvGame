# from model.character import Character
from model.scenario import Scenario
from model.character import Character

class CharacterTurn:
    @staticmethod
    def prompt_player(scenario: Scenario, tutorial: bool = False, user_input=input):
        char = scenario._character
        if tutorial: # TODO: finish implementing tutorial
            print("You have 2 actions per turn.")
            print("Moving and attacking both count as actions.")
            print("TODO")

        print("\nType the number of the option you want.")
        print("1. Move")
        # TODO: implement other actions, including attack

        while True:
            option = user_input("Option: ")
            if option == "1":
                if CharacterTurn.move(char):
                    break
            else:
                print("\nInvalid input. Please type the number cooresponding with the option.")

    @staticmethod
    def move(char: Character, user_input=input):
        print("\nType the direction and number of spaces you want to move.")
        while True:
            movement = user_input("Move: ")
            if len(movement) < 2:
                print("\nInvalid input. Please type the direction (+/-) and the number of spaces.")

            direction = movement[:1]
            spaces = movement[1:]
            if direction == "+" and direction == "-":
                if spaces.isdigits():
                    return char.move(direction, spaces)
                else:
                    print("\nInvalid input. After the direction, please type the number of spaces you want to move.")
            else:
                print("\nInvalid input. Please start with a + or - to for the direction you are moving in.")
        
