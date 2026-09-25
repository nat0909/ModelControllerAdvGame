from model.scenario import Scenario

class Formatting():
    @staticmethod
    def section_sub_title(section) -> str:
        title = f"\n{"-" * 100}\n{section.center(100)}\n{"-" * 100}\n"
        return title

    @staticmethod
    def section_title(section) -> str:
        title = f"\n\n{"=" * 100}\n\n{section.center(100)}\n\n{"=" * 100}\n\n"
        return title

    @staticmethod
    def display_board(scenario: Scenario) -> str:
        occupants = {}
        for abr, pos in scenario._positions.items():
            occupants[pos] = abr

        board = ""
        for space in range(1, scenario._spaces + 1):
            board += occupants.get(space, "__")
            board += " "
        return board 