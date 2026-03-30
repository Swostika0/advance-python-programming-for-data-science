#in multiple inheritance, there may be a situation that creates a diamond problem. 
# It is a situation where a class inherits from two classes that both inherit from a common base class. 
# This can lead to ambiguity when trying to access attributes or methods from the base class.

"""python solves this problem using the method resolution order (MRO) which is a set of rules that Python 
follows to determine the order in which classes are searched when looking for a method or attribute."""

class Class1:
    def m(self):
        print("In Class1")

class Class2(Class1):
    def m(self):
        print("In Class2")
        super().m()

class Class3(Class1):
    def m(self):
        print("In Class3")
        super().m()

class Class4(Class2, Class3):
    def m(self):
        print("In Class4")   
        super().m()
     
print(Class4.mro())         
print(Class4.__mro__)