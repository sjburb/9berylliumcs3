#1. a. Duck typing is a concept in Python where the type of an object is determined by its properties.
#   b. The speak and alive attribute.
#2. Code

class Car:
    def move(self):
        print("The car drives on the road.")

class Boat:
    def move(self):
        print("The boat sails on water.")

class Drone:
    def move(self):
        print("The drone flies in the sky.")

def start_trip(vehicle):
    vehicle.move()

car = Car()
start_trip(car)
boat = Boat()
start_trip(boat)
drone = Drone()
start_trip(drone)

#3. This code demonstrates polymorphism through duck typing.
