"""
Second Largest
Problem Description
You are given an integer array A. You have to find the second largest element/value in the array or report that no such element exists.


Problem Constraints
1 <= |A| <= 105
0 <= A[i] <= 109

Input Format
The first argument is an integer array A.

Output Format
Return the second largest element. If no such element exist then return -1.

Example Input
Input 1:
A = [2, 1, 2]

Input 2:
A = [2]

Example Output
Output 1:
1
Output 2:
-1
"""


def find_second_largest():
    try:
        A = list(map(int, input().split()))
        max1 = max(A)
        A.remove(max1)
        max2 = max(A)
        print(max2)
    except ValueError:
        print("-1")

    return 0

find_second_largest()



