from model.creature import Creature

class Goblin(Creature):
    def __init__(self, num: int):
        super().__init__(
            name=f"Goblin {num}",
            abreviation=f"G{num}",
            max_hit_points=10,
            dexterity=5,
            speed=3,
            melee_accuracy=4,
            melee_damage=2,
            ranged_accuracy=2,
            ranged_damage=2
        )
