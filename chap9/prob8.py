class Critter:
    def __init__(self, name, mood = 2):
        self.name = name
        self.mood = mood

    def setMood(self, mood):
        self.mood = mood

    def getMood(self):
        return self.mood
    
    def talk(self):
        if self.mood >= 4:
            print("I'm", self.name, "and I feel happy now.")
        elif self.mood == 3:
            print("I'm", self.name, "and I feel pleased now.")
        elif self.mood == 2:
            print("I'm", self.name, "and I feel frustradted now.")
        elif self.mood <= 1:
            print("I'm", self.name, "and I feel mad now.") 
        self.mood -= 1

    def feed(self, food):
        print("\nlololol.", food.name, "is very delicious!")
        food.setCritterLevel(self)

    def play(self):
        print("Wheee!")
        self.mood += 1
class Food:
    def __init__(self, name, level):
        self.name = name
        self.level = level

    def getLevel(self):
        return self.level

    def setCritterLevel(self, critter):
        critter.setMood(critter.getMood() + self.getLevel())
def main():
    crit_name = input("What do you want to name your critter?: ")
    crit = Critter(crit_name)
    food1 = Food("feedstuff", 3)
    food2 = Food("meet", 5)
    food3 = Food("cookie", 4)
    choice = None
    while choice != "0":
        print("""
        Critter Caretaker

        0 - Quit
        1 - Listen to your critter
        2 - Feed your critter
        3 - Play with your critter
        """)
        choice = input("Choice: ")
        print()

        if choice == "0":
            break;

        elif choice == "1":
            crit.talk()

        elif choice == "2":
            food_choice = input("""\tWhat food do you want to feed?

        1 - feedsstuff
        2 - meet
        3 - cookie\n\nChoice: """)      
            if food_choice == "1":
                crit.feed(food1)
            if food_choice == "2":
                crit.feed(food2)
            if food_choice == "3":
                crit.feed(food3)

        elif choice == "3":
            crit.play()

        else:
            print("Sorry,", choice, "isn't a valid choice.")

main()
