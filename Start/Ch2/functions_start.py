# LinkedIn Learning Python course by Joe Marini
# Example file for working with functions


# define a basic function
# def hello_func():
#   name = input("What is your name? :")
#   print("Nice to meet you,", name)

# call the function
# hello_func()

# function that takes parameters
# def hello_func2(greeting):
#   name = input("What is your name? :")
#   print(greeting)
#   print("Nice to meet you,", name)

# hello_func2("Greetings")
# hello_func2("Howdy")

# function that returns a value
# def cube(x):
#     return x * x * x

# result = cube(3)
# print(result)


# function with default value for an parameter
def hello_func3(greeting, name=None):
    if name is None:
        name = input("What is your name? :")
    print(greeting)
    print("Nice to meet you,", name)

hello_func3("Greetings", "Joe")

# function with variable number of parameters
def add_numbers(*args):
    total = 0
    for num in args:
        total += num
    return total

result = add_numbers(1, 2, 3, 4, 5)
print(result)
