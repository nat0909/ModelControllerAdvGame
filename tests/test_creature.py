from model.creature import Creature

class TestCreature:

    def create_creature(self):
        return Creature(
            "Goblin",
            "G1",
            10,
            5,
            3,
            4,
            2,
            2,
            2,
        )        

    def test_creature_constructor(self):
        sample_creature = self.create_creature()
        assert sample_creature._name == "Goblin"
        assert sample_creature._abr == "G1"
        assert sample_creature._hp == 10
        assert sample_creature._dex == 5
        assert sample_creature._speed == 3
        assert sample_creature._melee_acc == 4
        assert sample_creature._melee_dmg == 2
        assert sample_creature._ranged_acc == 2
        assert sample_creature._ranged_dmg == 2
    
    def test_set_max_hp(self):
        sample_creature = self.create_creature()
        sample_creature.max_hp(15)
        assert sample_creature._hp == 15
    
    def test_set_melee_accuracy(self):
        sample_creature = self.create_creature()
        sample_creature.melee_acc(5)
        assert sample_creature._melee_acc == 5
    
    def test_set_melee_damage(self):
        sample_creature = self.create_creature()
        sample_creature.melee_dmg(4)
        assert sample_creature._melee_dmg == 4
    
    def test_set_ranged_accuracy(self):
        sample_creature = self.create_creature()
        sample_creature.ranged_acc(3)
        assert sample_creature._ranged_acc == 3
    
    def test_set_ranged_damage(self):
        sample_creature = self.create_creature()
        sample_creature.ranged_dmg(1)
        assert sample_creature._ranged_dmg == 1