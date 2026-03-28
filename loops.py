#for loop
#example1
fruits = ["apple", "cherry", "banana", "papaya"]
for fruitName in fruits:
    print(fruitName)

#example2
n= "*"
for i in range(1,6):
    print(n*i)

#WHILE LOOPS with break and continue
"""syntax:while condition:
                do something
"""
#example1
count=0
while count<=5:
    print(count)
    count+=1
#example2 with break
a=1
while True:
    print(a)
    if a==5:
        break
    a+= 1
print("loop ended")
#example of continue with for
for i in range(1,10):
    if i%2==0:
        continue
    print(i)
#example of continue with while
j=0
while j<5:
    if j==3:
        j+=1
        continue
    print(j)
    j+= 1
print("loop ended")