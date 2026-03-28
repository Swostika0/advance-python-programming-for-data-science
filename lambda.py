#short one line codes are written
add = lambda x,y: x+y
print(add(10,20))

#lambda with map()
nums = [1,2,3,4,5]
# syntax example: squared_nums= list(map(function,iteration))
squared_nums= list(map(lambda x: x**2,nums))
print(squared_nums)

#lambda with filter()
nums = [1,2,3,4,5]
evens = list(filter(lambda x: x % 2==0, nums))
print(evens)

#lambda with reduce()--> convert whole list to one value
from functools import reduce
nums = [2,3,4]
product = reduce(lambda x,y: x * y, nums) #factorial jasto ho k yo
print(product)