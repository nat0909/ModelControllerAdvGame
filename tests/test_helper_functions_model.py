from model.helper_functions import HelperFunctions

class TestHelperFunctions():
    def test_interpret_input(self):
        input_options = ["apple", "banana", "apricot"]
        assert HelperFunctions.interpret_input("banana", input_options) == "banana"
        assert HelperFunctions.interpret_input("app", input_options) == "apple"
        assert HelperFunctions.interpret_input("b", input_options) == "banana"
        assert HelperFunctions.interpret_input("a", input_options) == "Unclear input"
        assert HelperFunctions.interpret_input("c", input_options) == "Invalid input"