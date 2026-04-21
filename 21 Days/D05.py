class Animals:
    def __init__(self, species):
        self.species = species

    def info(self):
        print(f"Species: {self.species}")

class Pets(Animals):
    def __init__(self, species, owner):
        super().__init__(species)
        self.owner = owner

    def show_owner(self):
        print(f"Owner: {self.owner}")


pet1 = Pets("Dog", "Jacob")

pet1.info()
pet1.show_owner()
