class Critter:
    """A vitual pet"""
    total =0
    def talk(self):
        print("Hi,I'm an instance of class Critter.")
    def __init__(self,name):
        Critter.total += 1
        self.name = name
        print("A critter has been born!")    
    def status():
        print("\nThe total number of critter is", Critter.total)

print("Accessing the class attribute Critter.total:", Critter.total)
print("\nCreating critters.")
crit1 = Critter("Critter 1")
crit2 = Critter("Critter 2")
crit3 = Critter("Critter 3")
Critter.status()
print("\nAccessing the class attribute through an object:", Critter.total)
