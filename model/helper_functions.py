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

    def closest_excluding(num: int, excluded: set, start_num: int, distance: int):
        """Find the value closest to num, reachable from start_num within distance and not in excluded.

        Args:
            num: The target value to get close to.
            excluded: Values to skip.
            start_num: The starting position.
            distance: Maximum reachable distance from start_num, cannot be negative.

        Returns:
            The closest reachable value to num that isn't in excluded, 
            preferring numbers closer to start_num on ties.
            If none are found, returns None.
        """

        possible_nums = []
        for cur in range(start_num - distance, start_num + distance + 1):
            if cur not in excluded:
                possible_nums.append(cur)

        if len(possible_nums) == 0:
            return None

        distances = map(lambda cur: abs(num - cur), possible_nums)
        
        min = -1 # placeholder
        min_index = None
        cur_index = 0
        for value in distances:
            if cur_index == 0 or value < min or (value == min and
            abs(start_num - possible_nums[cur_index]) < abs(start_num - possible_nums[min_index])):
                min = value
                min_index = cur_index
            cur_index += 1

        return possible_nums[min_index]