class Point:
    def __init__(self, x, y): # This is a constructor method,
        # which gets called when you intialise an object
        self.x = x
        self.y = y
    def move(self):
        print("Move")
    def draw(self):
        print("Draw")

# Constructor is a function that get called at the time of
# creating an object

point = Point(10,20)
print(point.x)
point.x = 40
print(point.x)

point1 = Point(10,20)
print(point1.x)

# Exercise

class Person:
    def __init__(self,name):
        self.name = name
    def talk(self):
        print(f"Hi , I am {self.name}")

person1 = Person("amotja")
person1.talk()
person1.name = "Anitha"

# each object is different instance of a classs

