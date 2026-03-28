#way of importing built-in modules

#way1--> this download all the functions and classe that were present in math module
import math
print(math.pi)
print(math.sqrt(25))

##way2 importing just the required function from a module
from math import sqrt
print(int(sqrt(16))) #yessai type casting gardeko show off hahaha

#way3 Aliasing aka giving a name to the module as user want to remember while accessing..WHATEVER!!!
import math as m
print(sqrt(625))