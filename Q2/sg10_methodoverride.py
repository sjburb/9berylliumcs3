class Animal:
    def __init__(self, name):
        self.name = name

    def eat(self):
        print("Animal eats food.")

    def make_sound(self):
        print("Animal makes sound!")


class Lion(Animal):
    def __init__(self, name):
      super().__init__(name)

    def eat(self):
        print(f"{self.name} eats fresh meat.")

    def make_sound(self):
        print(f"{self.name} roars loudly!")

class Elephant(Animal):
    def __init__(self, name):
      super().__init__(name)

    def eat(self):
        print(f"{self.name} eats grass and fruits.")
        
    def make_sound(self):
        print(f"{self.name} trumpets!")

class Monkey(Animal):
    def __init__(self, name):
      super().__init__(name)
        
    def eat(self):
        print(f"{self.name} eats bananas.")
                
    def make_sound(self):
        print(f"{self.name} chatters!")

lion = Lion("Simba")
elephant = Elephant("Dumbo")
monkey = Monkey("George")

lion.make_sound()
lion.eat()
print("-----")

elephant.make_sound()
elephant.eat()
print("-----")

monkey.make_sound()
monkey.eat()
print("-----")
