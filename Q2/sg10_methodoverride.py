class Animal: #Creates Animal class with the attributes name and methods eat and make_sound.
    def __init__(self, name):
        self.name = name

    def eat(self):
        print("Animal eats food.")

    def make_sound(self):
        print("Animal makes sound!")


class Lion(Animal): #Inherits name from Animal class.
    def __init__(self, name):
      super().__init__(name)

    def eat(self): #Overrides eat method from Animal class and gives it a specific food to eat instead of just food.
        print(f"{self.name} eats fresh meat.")

    def make_sound(self): #Overrides make_sound method from Animal class and gives it a specific sound to make instead of just makes sound.
        print(f"{self.name} roars loudly!")

class Elephant(Animal): #Inherits name from Animal class.
    def __init__(self, name):
      super().__init__(name)

    def eat(self): #Overrides eat method from Animal class and gives it a specific food to eat instead of just food.
        print(f"{self.name} eats grass and fruits.")
        
    def make_sound(self): #Overrides make_sound method from Animal class and gives it a specific sound to make instead of just makes sound.
        print(f"{self.name} trumpets!")

class Monkey(Animal): #Inherits name from Animal class.
    def __init__(self, name):
      super().__init__(name)
        
    def eat(self): #Overrides eat method from Animal class and gives it a specific food to eat instead of just food.
        print(f"{self.name} eats bananas.")
                
    def make_sound(self): #Overrides make_sound method from Animal class and gives it a specific sound to make instead of just makes sound.
        print(f"{self.name} chatters!")

lion = Lion("Simba") #Lion object that inherits name attribute from Animal class.
elephant = Elephant("Dumbo") #Elephant object that inherits name attribute from Animal class.
monkey = Monkey("George") #Monkey object that inherits name attribute from Animal class.

lion.make_sound() #Lion makes sound
lion.eat() #Lion eats
print("-----")

elephant.make_sound() #Elephant makes sound
elephant.eat() #Elephant eats
print("-----")

monkey.make_sound() #Monkey makes sound
monkey.eat() #Monkey eats
print("-----")
