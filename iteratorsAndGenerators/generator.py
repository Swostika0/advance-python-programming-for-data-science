#generator are the function that returns iterator object using yield instead of return
#example 1
def count():
    yield 1 #yield ia like an elevator stoping floor by floor
    yield 2 #pause-->print-->resume
    yield 3
    yield 4
    yield 100
for i in count():
    print(i)

#example2
def count(n):
    i = 1
    while i <= n:
        yield i 
        i += 1
for x in count(5):
    print(x)
