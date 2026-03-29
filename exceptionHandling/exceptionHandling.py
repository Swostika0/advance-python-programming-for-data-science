#there is  various methods of exception handling
#way1 --> try and except
#whenever user inputs some values like 0 or any strings it doesnot throw any error but it runs the except wala code
try:
    a=int(input("enter a number: "))
    b=10/a
    print("Result: ",b)
except:
    print("Something went wrong") 

#way2 --> catch ie not every errors are same so using kind of errors with except for diff. possible errors
try:
    a=int(input("enter a number: "))
    b=10/a
    print("Result: ",b)
except ValueError:
    print("please enter valid number") 
except ZeroDivisionError:
    print("NUmbers cant be divided by 0") 

#handling multiple exception with only one except
try:
    a=int(input("enter a number: "))
    b=10/a
    print("Result: ",b)
except (ValueError,ZeroDivisionError):
    print("Invalid number") 

#way4--> using else and finally
#using else-- codes run only when try block succeeds
try:
    num=int(input("Enter Age: "))
except ValueError:
    print("invalid input")
else:
    print("your age is: ",num)

#using finally--> runs every time even if theres error or not
try:
    num=int(input("Enter Age: "))
except ValueError:
    print("invalid input")
else:
    print("your age is: ",num)
finally:
    print("execution completed")


