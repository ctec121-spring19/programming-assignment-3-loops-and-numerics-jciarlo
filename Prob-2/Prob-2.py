# Module 2
#   Programming Assignment 3
#     Prob-2.py

# Jonathan Ciarlo

def example():
    print("\nExample Output")
   # section 1
    x = 5
    # print x and its type
    print("x", x, "is a", type(x))

    # section 2
    print()
    x = float(x)
    print("x", x, "is a", type(x))

def studentCode():
    print("\nStudent Output")
    # section 1
    x = 5
    y = 3.14
    z = "a string"

    # print the values for x, y, and z and their types each on a separate line
    print("x", x, "is a", type(x))
    print()
    print("y", y, "is a", type(y))
    print()
    print("z", z, "is a", type(z))
    print()
    # section 2
    # convert y to an int and print

    y = 9.99
    print(int(y))
    # convert y to an int and print
    print(int(y))
    print()

    z = "12.34"
    # print z and its type
    print("z", z, "is a", "<class 'float'>")
    # use eval() to convert z to a number and print its value and type
    print(eval(z), "is a", "<class 'float'>")

    print()

example()
studentCode()