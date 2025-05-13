# LinkedIn Learning Python course by Joe Marini
# Example file for variables and basic types


# Basic data types in Python: Numbers, Strings, Booleans, sequences, and Dictionaries
# Variable names must start with a letter or _, and can have numbers. They are case sensitive. 
myint = 10
myfloat = 13.2576
mystr = "This is a string"
mybool = True

#Naming rules
# Variable names can only contain letters, numbers, and underscores
# Variable names cannot start with a number
# Variable names cannot be a keyword
# Variable names are case sensitive
# Variable names should be descriptive and meaningful


# We can display the content of a variable using the print() function
print(myint)
print(mystr)

# Operators are used to perform operations on variables
print(myint + 5) # addition
print(myint - 5) # subtraction
print(myint * 5) # multiplication
print(myint / 5) # division
print(myint % 3) # modulus

# Logical and comparison operators 
print(myint == 10) # equal to
print(myint != 10) # not equal to
print(myint > 5) # greater than
print(myint < 5) # less than


# re-declaring a variable works
myint = 20
print(myint)
