"""my_set={7,2,3,4,6,9,5,3} #ignores duplicate value prints 3 only once
print(my_set)
print(type(my_set))
print(len(my_set))

my_set.add("swosti")
print(my_set)
my_set.remove("me") #shows error as it wont find that string in the set
my_set.discard("me")#no error even it wont find me
my_set.pop() #remove random element
"""

#sets method
set1= {1,2,3,4}
set2={3,4,5,6}
print(set1.union(set2))
print(set1.intersection(set2))
print(set1.difference(set2))
print(set1.symmetric_difference(set2))