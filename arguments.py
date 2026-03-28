#non keyword arguments(*args)
def make_pizza(size,*toppings): #pass list as an arguments
    print(f"\nMaking a {size} pizza wee need following toppings.")
    for topping in toppings:
        print(f"-{topping}")
make_pizza(16,"pepperon", "mushroom","extracheese")

#keyword arguments(**kwargs)
def build_profile(first,last,**user_info): #pass dictionary as arguments
    profile ={'first-name':first,'last-name':last,'user_info':user_info}#this creates a nested dictionary
    return profile
user_profile = build_profile('swostika','bajagain',location='tikabhairab',field = 'frontend')
print(user_profile)

def build_profile(first,last,**user_info): #pass dictionary as arguments
    profile ={'first-name':first,'last-name':last}
    profile.update(user_info) #yesto garena vani first ra last matra print huncha,this will create a single normal dictionary
    return profile
user_profile = build_profile('swostika','bajagain',location='tikabhairab',field = 'frontend')
print(user_profile)

#*args and**kwargs together-->the order should be *args followed by **kwargs
def print_details(name,*hobbies,**kwargs):
    print(f"name:{name}")
    print(f"hobbies:{hobbies}") #arg for list
    print(f"keyword arguments:{kwargs}") #kwargs for dictionary
print_details('pihu','dance','code',city='lalitpur',age='23')

