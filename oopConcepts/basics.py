#creating class and object
class Dog:
    species = "canine"
    def __init__(self,name,age):
        self.name=name
        self.age=age
        print(f"i am a constructor function for {self.name}")
    def display(self):
        print(f"the name of the dog is {self.name} and it is {self.age} years old.It belongs to {self.species} family")
    def __del__(self):
        print(f"i am a destructor function for {self.name}")


#creating object
Dog("coco",2) # this runs only the code inside constructor(not stored BTW)
d1=Dog("kuki",1.5)
d1.display()
del d1 # automatically delete ta hunthyo ie destructor runs without it but it is used for -->forcefully delete object immediately
