#Task 1

class Pet():

    def __init__(self,name,species, hunger=5,happiness=5,energy=10):
        self.name = name
        self.species= species
        self.hunger = hunger
        self.happiness = happiness
        self.energy = energy

    def feed(self):
        if self.hunger>=3:
            self.hunger -= 3
            self.energy+=1

        elif self.hunger<3:
            print(f'{self.name} is almost dying. Feed him!')

    def play(self):
        self.happiness+=2
        self.energy -= 2
        self.hunger += 1

    def sleep(self):
        self.energy = 10

    def status(self):
        print(f"{self.name} ({self.species}): hunger={self.hunger}, happiness={self.happiness}, energy={self.energy}")

pet = Pet("Rex", "Dog")
pet.status()
pet.play()
pet.feed()
pet.sleep()
pet.status()




