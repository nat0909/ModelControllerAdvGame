from model.enemy import Enemy

class Goblin(Enemy):
    def __init__(self, num: int):
        super().__init__(
            name=f"Goblin {num}",
            abreviation=f"G{num}",
            max_hit_points=10,
            dexterity=8,
            speed=5,
            melee_accuracy=4,
            melee_damage=2,
            ranged_accuracy=2,
            ranged_damage=1
        )

    def turn(self, positions: list, gob_in: int):
        pos = positions[gob_in]
        enemy_pos = positions[0]

        attack_type = "none"
        new_pos, melee_attack = self.move_towards(positions, gob_in)
        if melee_attack:
            attack_type = "melee_attack"
        elif abs(pos - enemy_pos) <= 20:
            attack_type = "ranged_attack"

        return new_pos, attack_type
        