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

    def perform_turn(self, positions: dict, char_abr: str) -> tuple[int, str]:
        pos = positions[self._abr]
        enemy_pos = positions[char_abr]

        attack_type = "none"
        new_pos = self.move_towards(positions, char_abr)
        if new_pos == enemy_pos + 1 or new_pos == enemy_pos - 1:
            attack_type = "melee_attack"
        elif abs(pos - enemy_pos) <= 20:
            attack_type = "ranged_attack"

        return new_pos, attack_type

    def move_towards(self, positions: dict, char_abr: str) -> int:
        char_pos = positions[char_abr]
        self_pos = positions[self._abr]
        distance = self._speed

        occupied = set(positions.values())
        occupied.discard(self_pos)

        reachable_positions = {}
        for cur_pos in range(self_pos - distance, self_pos + distance + 1):
            if cur_pos not in occupied:
                reachable_positions[(abs(cur_pos - char_pos), abs(cur_pos - self_pos))] = cur_pos

        distances = reachable_positions.keys()
        return reachable_positions[min(distances)]

    def move_away():
        return # TODO: enemies specializing in ranged attacks move away from the character
    
