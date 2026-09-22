class TurnLog:
    def __init__(self, creature_name: str, old_position: int, new_position: int): # TODO: attack_hit: bool, damage: int
        self._name = creature_name
        self._old_position = old_position
        self._new_position = new_position
        # self._attack_hit = attack_hit
        # self._damage = damage # -1 = attacked missed, no damage

    