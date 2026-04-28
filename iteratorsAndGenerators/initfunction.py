#actually __init__ is a constructor method
class const:
    def __init__(self):
        print("Object created")
c1 = const()
print(c1)
#example2
class Student:
    def __init__(self, name,roll):
        self.name = name
        self.roll = roll

s1 = Student("Pihu",4)
print(s1.name)
s2 = Student("swosti",16)
print(f"I am {s2.name} and my age is {s2.roll}" )
