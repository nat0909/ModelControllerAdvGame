from model.helper_functions import HelperFunctions

class CharacterCreation():
    def choose_name(user_input=input):
        print("\nPick a name for your character.")
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




