"""
Class Variables are common to the class.
They are not included in __init__() function
"""
class Human:
    population = 0
    data = []
    def __init__(self, name, age, migrate=True):
        self.name = name
        self.age = age
        self.migrate = migrate
        Human.population += 1
        Human.data.append(self.name)
    def migration(self):
        if self.migrate:
            print(f"{self.name} has migrated to another country")
            Human.population -= 1
            Human.data.remove(self.name)
            self.migrate = False
        else:
            print(f"{self.name} has already migrated")
h = Human("Manbir", 22)
#print(Human.population)
h1 = Human("Kashleen", 21)
#print(Human.population)
h2 = Human("Naman", 22)
print(f"Total number of humans: {Human.population}")
print(f"List of them:{Human.data}")
h1.migration()
h1.migration()
print(f"Total number of humans: {Human.population}")
print(f"List of them:{Human.data}")