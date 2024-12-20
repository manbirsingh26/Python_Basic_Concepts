import random
import string
from collections import Counter


def solve(A, B):
    # Replace all '?' in A with random letters
    A = ''.join(random.choice(string.ascii_letters) if char == '?' else char for char in A)

    # Count the frequency of each character in A and B
    count_A = Counter(A)
    count_B = Counter(B)

    # Count how many characters have the same frequency in A and B
    counter = sum(1 for char in count_A if count_A[char] == count_B.get(char, 0))

    return counter
A = "a?c?e"
B = "abc"
result = solve(A, B)
print(result)
