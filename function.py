#nonparameterized function
def greet():
    print("hello")
greet()

#parametrized function
def sum(num1,num2): #parameter are num1 and num2
    print("the sum is",num1+num2)
sum(10,20) #arguments are passed as parameter
sum(83,66)

def greet(name):
    print("hello",name)
greet("swostika")

#return
def sum(num1,num2): #parameter are num1 and num2
    return num1+num2 #return nagari add ma value dinai mildaina
add=sum(10,20) #arguments are passed as parameter
print(add)
#note that return nagari aauni resultlai variable = garnu mildaina

#DEFAULT parameter(used a lot in big projects)
def multiply(a=3,b=4):
    print("the product is: ",a*b)
    return a*b
output = multiply()
print ("the output of the multiply function is: ",output)