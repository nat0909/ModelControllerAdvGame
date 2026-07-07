import copy

class HelperFunctions():
    # Returns the option in array options that best matches input
    # NOTE: currently not being used
    def interpret_input(input, options: list):
        options_copy = copy.deepcopy(options)

        for i in range(len(input)):
            ch = input[i]
            for option in options_copy[:]:
                try:
                    if option[i] != ch:
                        options_copy.remove(option)
                except IndexError:
                    options_copy.remove(option)

        num_of_options = len(options_copy)
        if num_of_options == 1:
            return options_copy[0]
        elif num_of_options == 0:
            return "Invalid input"
        else:
            return "Unclear input"
