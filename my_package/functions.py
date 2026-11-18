# a function to add three numbers

# def add(a, b, c):
#     return a + b + c


# print(add(7, 7, 7))
# A function that can take multiple parameters
def addition(*nums): # one * because it will be a list
    total = sum(nums)
    return total

# A function that will build the profle of a person

def build_profile(**kwargs):# 2 ** Because its going to use a dictionary
    for k, w in kwargs.items():
        print(f"{k} : {w}")

# build_profile(firstname='jerry', age=18, nationality='Kenyan', experience='five years')


# A function that takes in lists, dictionaries and variables
def fancy_function(name, *nums, **kwargs):
    numbers = sum(nums)
    for key, value in kwargs.items():
        total = value * numbers
        print(f"Hey {name} This is your out put {total}")


# fancy_function('Naomi', 30, 20, 50, digit = 2)

# Anonymous functions called lambda

adding = lambda x, y: sum([x,y]) # To pass two values into sum we use [] if not we get an error

# print (adding(10, 9))

square = lambda num : num * num

# print(square(5))

surface_area_cylinder = lambda r, h: 22/7 * r**2 * 2 + 22/7 * r*2 * h

# print(surface_area_cylinder(7, 20))


people = [{"firstname" :"Jane", "age":20},
          {"firstname" :"Paul", "age":21},
          {"firstname" :"Simon", "age":25},
          {"firstname" :"Anne", "age":55}]


sorted_people_name = sorted(people, key= lambda x: x["firstname"], reverse= False)

print(sorted_people_name)









# print(addition(45, 70, 35, 14))
