def hello():
    """what is this part 1"""

    print("Hello World!")

    """what is this part 3"""

"""
what is this
"""

hello()


def what():
    print('hihiahah')

    """what is this part 2"""

    print('drishyam 2')

# function needs to be imported before or defined before before it is called
what()

print(what.__annotations__)
print(what.__doc__)
print(hello.__doc__)

# only the first part docstring is taken as function doc not anything else
