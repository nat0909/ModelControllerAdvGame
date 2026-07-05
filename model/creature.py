class Creature:
    def __init__(self, name: str, abreviation: str, max_hit_points: int, dexterity: int, melee_accuracy: int, melee_damage: int, ranged_accuracy: int, ranged_damage: int):
        self._name = name
        self._abr = abreviation
        self._hp = max_hit_points
        self._dex = dexterity
        self._melee_acc = melee_accuracy
        self._melee_dmg = melee_damage
        self._ranged_acc = ranged_accuracy
        self._ranged_dmg = ranged_damage

    # Setters
    def max_hp(self, hp):
        self._hp = hp

    def melee_acc(self, acc):
        self._melee_acc = acc

    def melee_dmg(self, dmg):
        self._melee_dmg = dmg
    
    def ranged_acc(self, acc):
        self._ranged_acc = acc

    def ranged_dmg(self, dmg):
        self._ranged_dmg = dmg