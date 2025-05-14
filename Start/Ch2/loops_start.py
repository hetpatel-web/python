# LinkedIn Learning Python course by Joe Marini
# Example file for working with loops


x = 0

# define a while loop
# while x < 5:
#     print("x is currently: ", x)
#     x += 1
# print("Done with while loop")
# print("value of x after while loop: ", x)

# answer = input("stop? (y/n): ")
# while answer != "y":
#     print(answer)
#     answer = input("stop? (y/n): ")

# define a for loop
days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
# for d in days:
#     print(d)

# use a for loop over a collection


# use the break and continue statements
for d in days:
    if d == "Wed":
        print("found Wednesday")
        break
    print(d)

# use the continue statement to skip an iteration
for d in days:
    if d == "Wed":
        print("found Wednesday")
        continue
    print(d)

# using the enumerate() function to get an index and an item
for i, d in enumerate(days):
    print(i, d)