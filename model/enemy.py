from model.creature import Creature

class Enemy(Creature):
    def __init__(self, name: str, abbreviation: str, max_hit_points: int, dexterity: int, speed: int, melee_accuracy: int, melee_damage: int, ranged_accuracy: int, ranged_damage: int):
        super().__init__(
            name, 
            abbreviation,
            max_hit_points, 
            dexterity, 
            speed,
            melee_accuracy, 
            melee_damage, 
            ranged_accuracy, 
            ranged_damage
        )

    def move_towards(self, positions: list, index: int):
        pos = positions[index]
        char_pos = positions[0]
        
        new_pos = pos
        next_to_char = False
        # get as close as possible to the character, don't move more then neccessary to achieve this
        if pos != char_pos:
            distance = abs(pos - char_pos)
            direction = 1 if pos < char_pos else -1
            if distance + 1 <= self._speed:
                next_to_char = True
                new_pos = char_pos - direction
            else:
                new_pos = pos + direction * self._speed

            occupied = set(positions)
            set.remove(pos)
            if new_pos in occupied:
                reachable = [
                    p for p in range(pos - self._speed, pos + self._speed + 1)
                    if p != char_pos and p not in occupied
                ]

            # occupied = set(positions[i] for i in range(len(positions)) if i != index)
            # if new_pos in occupied:
            #     next_to_char = False
            #     reachable = [
            #         p for p in range(pos - self._speed, pos + self._speed + 1)
            #         if p != char_pos and p not in occupied
            #     ]
            #     if reachable:
            #         new_pos = min(reachable, key=lambda p: (abs(p - char_pos), p * direction))
            #         if abs(new_pos - char_pos) == 1:
            #             next_to_char = True
            #     else:
            #         new_pos = pos

        return new_pos, next_to_char
    
    def move_away():
        return # TODO: enemies specializing in ranged attacks move away from the character
    
