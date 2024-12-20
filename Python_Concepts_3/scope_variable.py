"""
There are two scopes of a variable:-
1. Global Scope: A global variable can be used anywhere in the program
2. Local Scope: A local variable can only be used locally inside a function(in which it is declared)

Declaring Global Variable:-
1. If it is declared outside the function then automatically it is a global variable
2. But in order to alter(change value of) a global variable inside a function we have to use "global" keyword
"""
a = 20   #Global variable

def func():
    x = 25
    print(f"Value of local x:{x}")
    global a
    a = a + 10
print(f"Value of global a before alter:{a}")
func()
print(f"Value of global a after altering:{a}")
#print(x)  #If we try to do this, it will generate NameError because x is a local variable

