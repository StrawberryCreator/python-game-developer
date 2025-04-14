print ("="*50)
class car:
    def __init__ (self, acceleration, speed, maxSpeed, color, brand):
        self.acceleration = acceleration
        self.speed = speed
        self.maxSpeed = maxSpeed
        self.color = color
        self.brand = brand
    def carDetails (self):
        print (f"acceleration {self.acceleration}")
        print (f"speed {self.speed}")
        print (f"maxSpeed {self.maxSpeed}")
        print (f"color {self.color}")
        print (f"brand {self.brand}")
    def seedUp (self):
        if self.speed >= self.maxSpeed:
            print ("Achieved maximum speed")
        else:
            self.speed += self.acceleration
            print (f"speed {self.speed}")
    def brake (self):
        if self.speed <= 0:
            self.speed = 0
            print ("Car is fully stopped")
        else:
            self.speed -= self.acceleration*2
            if self.speed < 0:
                self.speed = 0
            print (f"speed {self.speed}")

car_ = car (15, 0, 75, "red", "toyota")
car_.carDetails ()
print ("- "*25)
action = ""
while action != "cancel":
    action = input("Do you want to speed up, brake or cancel? ")
    if action == "speed up":
        car_.seedUp ()
    elif action == "brake":
        car_.brake ()
    elif action == "cancel":
        print ("Car stopped")
    else:
        print ("Invalid action")
    print ("-   "*13)

print ("="*50)