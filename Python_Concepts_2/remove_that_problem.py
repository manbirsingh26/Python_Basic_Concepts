"""
Remove that

Problem Description
Write a program to input N numbers array, A from the user and an integer X and print the array by deleting element at specified position X.
Note: The first element is located at position 1, the second element is located at position 2, and so on.


Problem Constraints
2 <= N <= 100
1 <= A[i] <= 1000
1 <= X <= N


Input Format
First line is N which means number of elements.
Second line contains N space separated integers.
Third line is X position which has to be deleted.


Output Format
N-1 space separated integers of the input array after deleting the element at required position.



Example Input
Input 1:

5
2 3 1 4 2
3

Input 2:

2
4 5
2



Example Output
Output 1:

2 3 4 2

Output 2:
4
"""


def remove():
    N = int(input())
    lis = list(map(int, input().split()))
    X = int(input())
    if 1 <= X < N:
        lis.remove(lis[X-1])
    print(" ".join(map(str, lis)))
    return lis

remove()

