"""
Is It Identity Matrix?
Problem Description
You are given a N X N square integer matrix A. You have to tell whether A is an identity matrix or not.
Identity matrix is a special square matrix whose main diagonal elements are equal to 1 and all other elements are 0.

Problem Constraints

2 <= N <= 103

A[i][j] equals 0 or 1.

Input Format
The first argument is a 2D integer array denoting the matrix A

Output Format
Return 1 if A is an identity matrix, else return 0.

Example Input
Input 1:
[[1, 0], [0, 1]]

Input 2:
[[0, 0, 1], [0, 1, 0], [1, 0, 0]]

Example Output
Output 1:
1

Output 2:
0

"""


def identity_matrix():
    N = int(input())
    A = [list(map(int, input().split())) for _ in range(N)]
    for i in range(0, N):
        for j in range(0, N):
            if i == j and A[i][j] == 1:
                res = 1
            else:
                res = 0

    print(res)

    return 0


identity_matrix()
