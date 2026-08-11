from model.helper_functions import HelperFunctions

class TestHelperFunctions():
    def test_interpret_input(self):
        input_options = ["apple", "banana", "apricot"]
        assert HelperFunctions.interpret_input("banana", input_options) == "banana"
        assert HelperFunctions.interpret_input("app", input_options) == "apple"
        assert HelperFunctions.interpret_input("b", input_options) == "banana"
        assert HelperFunctions.interpret_input("a", input_options) == "Unclear input"
        assert HelperFunctions.interpret_input("c", input_options) == "Invalid input"

    def test_closest_excluding(self): # TODO: remove
        assert HelperFunctions.closest_excluding(10, [10], 5, 10) == 9
        assert HelperFunctions.closest_excluding(10, [10], 15, 10) == 11
        assert HelperFunctions.closest_excluding(10, [], 5, 10) == 10
        assert HelperFunctions.closest_excluding(0, [0, 1], 5, 10) == -1
        assert HelperFunctions.closest_excluding(10, [], 5, 2) == 7
        assert HelperFunctions.closest_excluding(10, [6, 7], 5, 2) == 5
        assert HelperFunctions.closest_excluding(10, [4, 5, 6, 7], 5, 2) == 3
        assert HelperFunctions.closest_excluding(10, [3, 4, 5, 6, 7], 5, 2) == None