from controller.formatting import Formatting
import time

class CharacterCreation():
    def create_character(user_input=input):
        Formatting.section_title("Character Creation")
        name = CharacterCreation.choose_name()
        char_class = CharacterCreation.choose_class()
        max_hp, dex, speed, melee_acc, melee_dmg, ranged_acc, ranged_dmg = CharacterCreation.determine_stats(char_class)

        print("\nCreating character...")
        time.sleep(2)

        Formatting.section_title(name)
        print("Class:", char_class.title())
        print("\nMax Hit Points:", max_hp)
        print("Dexterity:", dex)
        print("Speed:", speed)
        print("\nMelee Accuracy:", melee_acc)
        print("Melee Damage:", melee_dmg)
        print("Ranged Accuracy:", ranged_acc)
        print("Ranged Damage:", ranged_dmg)

    def determine_stats(c):
        # Base stats
        max_hp = 20
        dex = 2
        speed = 3
        melee_acc = 2
        melee_dmg = 2
        ranged_acc = 2
        ranged_dmg = 2

        if c == "warrior":
            max_hp += 10
            dex += 2
            melee_acc += 4
            melee_dmg += 2
        elif c == "ranger":
            speed += 5
            ranged_acc += 4
            ranged_dmg += 2
        elif c == "rogue":
            dex += 4
            speed += 3
            melee_acc += 4
            ranged_acc += 4

        return max_hp, dex, speed, melee_acc, melee_dmg, ranged_acc, ranged_dmg

    def choose_name(user_input=input):
        print("Pick a name for your character.")
        while True:
            name = user_input("Name: ").strip()       
            if name.isalpha():
                return name.title()
            else:
                print("\nThe name may not have any numbers, spaces, or special characters.")
                print("Please choose another name.")
    
    def choose_class(user_input=input):        
        print("\nWrite the number of the class you want.")
        print("1. Warrior")
        print("2. Ranger")
        print("3. Rogue")

        while True:
            class_num = user_input("Class: ").strip().lower()
            if class_num == "1":
                return "warrior"
            elif class_num == "2":
                return "ranger"
            elif class_num == "3":
                return "rogue"
            else:
                print("\nInvalid input. Please type the number cooresponding with the class.")





