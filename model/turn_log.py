class TurnLog:
    def __init__(self, creature_name: str, old_position: int, new_position: int, attack_hit: bool, damage: int):
        _name = creature_name
        _old_position = old_position
        _new_position = new_position
        _attack_hit = attack_hit
        _damage = damage # -1 = attacked missed, no damage

    