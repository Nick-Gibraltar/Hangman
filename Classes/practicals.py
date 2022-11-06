import math

class Cylinder:

    def __init__(self, height, radius=1):
        
        self.height = height
        self.radius = radius
        self.surface_area = None
        self.volume = None
    
    def get_surface_area(self):
        self.surface_area = 2 * math.pi * self.radius * (self.height + self.radius)

    def get_volume(self):
        self.volume = math.pi * self.radius * self.radius * self.height

class Car:

    def __init__(self, model, year=2022):

        self.model = model
        self.year = year
        self.miles_driven = 0

    def drive(self):
        
        print("Vroom!")
        self.miles_driven +=1

    def info(self):

        print(f"Miles driven: {self.miles_driven}, Model name: {self.model}, Year: {self.year}")

class Vector:

    def __init__(self, numbers):
        self.numbers = numbers
    
    def __repr__(self):
        return "|" + ",".join([str(i) for i in self.numbers]) + "|"      
   
    def __add__(self, other):
        add_list = [x+y for x,y in zip(self.numbers, other.numbers)]
        return Vector(add_list)

    def __gt__(self, other):
        return self.magnitude() > other.magnitude()

    def __getitem__(self, i):
        return self.numbers[i]

    def magnitude(self):
        mag = math.sqrt(sum([i*i for i in self.numbers]))
        return mag


testvector = Vector([1,2,3,4,5,6])
print(testvector)
anothervector = Vector([9,8,3,456,-15,4])
print(anothervector)
total = testvector + anothervector
print(testvector.magnitude())
print(anothervector.magnitude())
print(testvector>anothervector)
for i in range(6):
    print(testvector[i], anothervector[i], total[i])

import datetime

class Person:

    def __init__(self, friends, name=None, date_of_birth=None):

        self.name = name
        self.date_of_birth = date_of_birth
        self.friends = friends

    def __str__(self):
        dob_string = self.date_of_birth.strftime("%Y")+self.date_of_birth.strftime("%m")+self.date_of_birth.strftime("%d")
        person_string = f"Name: {self.name} DOB: {dob_string} Friends: {len(self.friends)}"
        return person_string

    def add_friend(self, other):
        self.friends.append(other.name)
        other.friends.append(self.name)


person1 = Person(["A","B","C"], "Big", datetime.date(1972,5,20))
person2 = Person(["D"], "Small", datetime.date(1975,10,10))

#print(person1,person2)
#person1.add_friend(person2)
#print(person1,person2)

class Shape:

    def __init__(self, num_sides, tesselates=None):
        if num_sides == 0:
            raise ValueError

        self.num_sides = num_sides
        self.tesselates = tesselates

    def get_info(self):
        #raise NotImplementedError
        return f"Sides: {self.num_sides} Tesselates: {self.tesselates}"
    
    def __add__(self,other):
        return Shape(self.num_sides + other.num_sides)

class Circle(Shape):
    def __init__(self):
        super().__init__(1, False)

class Triangle(Shape):
    def __init__(self):
        super().__init__(3, False)

class Square(Shape):
    def __init__(self):
        super().__init__(4, True)

class Pentagon(Shape):
    def __init__(self):
        super().__init__(5, False)

class Hexagon(Shape):
    def __init__(self):
        super().__init__(6, True)




testshape = Hexagon()
othershape = Square()
print(testshape.get_info(), othershape.get_info())
newshape = testshape+othershape
print(newshape.get_info())

