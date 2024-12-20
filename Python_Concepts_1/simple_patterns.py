"""
Print the following pattern:-
$
$ $
$ $ $
$ $ $ $
$ $ $ $ $
"""
for i in range(1, 6):
    print("$ "*i)

"""
Print the following pattern:-
$ $ $ $ $
$ $ $ $ $
$ $ $ $ $
$ $ $ $ $
$ $ $ $ $
"""
for i in range(1, 6):
    print("$ "*5)

"""
Print the following pattern:-
$ $ $ $ $ 
$ $ $ $ 
$ $ $ 
$ $ 
$ 
"""
for i in range(5, 0, -1):
    print("$ "*i)
"""
Print the following pattern:-
$
$ $
$ $ $
$ $ $ $
$ $ $ $ $ 
$ $ $ $ 
$ $ $ 
$ $ 
$ 
"""
for i in range(1, 6):
    print("$ "*i)
for j in range(4, 0, -1):
    print("$ "*j)

"""
Print the following pattern:-
*         *
* *     * *
*  *   *  *
*   * *   *
*    *    *
"""
#Simplest approach
print("*         *")
print("* *     * *")
print("*  *   *  *")
print("*   * *   *")
print("*    *    *")
#using for loop
n = 5  # Number of rows
for i in range(n):
    for j in range(2 * n - 1):
        if j == 0 or j == 2 * n - 2 or j == i or j == 2 * n - 2 - i:
            print('*', end='')
        else:
            print(' ', end='')
    print()





