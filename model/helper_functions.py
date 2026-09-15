import copy

class HelperFunctions():
    # NOTE: currently not being used
    @staticmethod
    def interpret_input(input, options: list):
        """Find the option that best matches the input.
        
        Args:
            input: The variable checked with.
            options: Variables to check against. 
            
        Returns: 
            The variable in options that best matches input."""

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