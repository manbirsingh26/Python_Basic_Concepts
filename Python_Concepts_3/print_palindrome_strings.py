"""
Given a list of stings, check and print only the palindrome strings in a new list(where string = reverse(string)
"""
def palindrome(A):
    res = []
    for x in A:
        if x[::-1] == x:
            res.append(x)
    print(res)
    return res

palindrome(["manbir", "naman", "mam", "sis", "kashleen"])
s = ["abc", "abba", "abab", "baab"]
palindrome(s)
