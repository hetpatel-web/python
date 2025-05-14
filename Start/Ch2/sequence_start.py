# LinkedIn Learning Python course by Joe Marini
# Example file for complex types

# Sequences: Lists and Tuples
# These are -- surprise -- sequences of values
mylist = [1, 2, 3, 4, 5]
mylist2 = ["a", "b", "c", "d", "e"]
mylist3 = [1, 2, 3, "a", "b", "c"]
mylist4 = [1, 2, 3, [4, 5, 6], "a", "b", "c"]

print(len(mylist))  # get the length of a list

# to access a member of a sequence type, use []
print(mylist[0])  # to access a member of a sequence type, use []
print(mylist[-1])  # negative index to access from the end of the list

mylist[0] = 10  # change a value in the list
print(mylist)  # print the list after changing a value
# add a list to another list
mylist += mylist2  # add a list to another list


# use slices to get parts of a sequence
print(mylist[1:3])  # get a slice of the list
print(mylist[1:3:2])  # get a slice of the list with a step
print(mylist[::2])  # get a slice of the list with a step


# you can use slices to reverse a sequence
print(mylist[::-1])  # reverse the list

# Tuples are like lists, but they are immutable
myTuple = (1, 2, 3, 4, 5, "six")
print(myTuple[0])  # to access a member of a sequence type, use []

# Sets are also sequences, but they contain unique values
myset = {1, 2, 3, 4, 5, "six", "seven", "eight", "nine", "ten"}
print(myset)  # print the set
# Sets are unordered collections of unique elements
print(1 in myset)  # test for membership


# Set, however, can not be indexed like lists or tuples
# print(myset[0]) # this will cause an error

# Test for membership
