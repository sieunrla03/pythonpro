class Critter:
    """A virtual pet"""
    total = 0

    def talk(self):
        print("\nHi, I'm", self.name)
    def __init__(self, name):
        print("A new critter has been born!")
        self.__name = name
    def get_name(self):
        return self.__name
    def set_name(self, new_name):
        if new_name == "":
            print("A critter's name can't be the empty string.")
        else:
            self.__name = new_name
            print("Name change successful.")
    name = property(get_name, set_name)

crit = Critter("Poochie")
crit.talk()

print("\nMy critter's name is:", end=" ")
print(crit.get_name())

print("\nAttempting to change my critter's name")
crit.name = ""

print("\nAttempting to change my critter's name again.")
crit.name = "Randolph"
print("\nHi, I'm", end=" ")
print(crit.get_name())
