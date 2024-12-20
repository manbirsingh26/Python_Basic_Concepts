print(print.__doc__)  # This is format to read docstring of a function in Python
print(range.__doc__)

# Creating a docstring for a function
def even_odd():
    """
even_odd():This function checks whether the entered number is even or odd
    """
    a = int(input("Enter number: "))
    if a % 2 == 0:
        print("Even")
    else:
        print("Odd")
    return 0
#even_odd()   #Calling the function
print(even_odd.__doc__)

