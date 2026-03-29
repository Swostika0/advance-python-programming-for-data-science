"""#example :1
class MyIterator:
    def __init__(self):
        self.num = 1   # starting value

    def __iter__(self):
        return self   # iterator object return

    def __next__(self):
        if self.num <= 5:
            value = self.num
            self.num += 1
            return value
        else:
            raise StopIteration   # end of iteration
obj = MyIterator()

for i in obj:
    print(i)"""

#example-2
class countUpto:
    def __init__(self,max):
        self.max=max #maximum kati samma jani vanni ho
        self.current = 1 #starting point 1 bata start huncha
    def __iter__(self):
        return self
    def __next__(self):
        if self.current <= self.max:
            val = self.current
            self.current += 1
            return val
        else:
            raise StopIteration
for i in countUpto(5):
    print(i)
