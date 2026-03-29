#lets learn the built in iterator
#it must include iter() and next()
nums = [1, 2, 3]

it = iter(nums) #creates iterator

print(next(it))  # 1 #retrives character one by one
print(next(it))  # 2
print(next(it))  # 3
#now we know all elements in the list are traversed and if we still try to print it shows stopIterationError
"""print(next(it))"""
