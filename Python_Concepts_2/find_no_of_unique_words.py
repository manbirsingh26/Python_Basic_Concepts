"""
Given a sentence, find the number of unique words in the sentence
"""
a = str(input("Enter the sentence: "))
words = a.split()
unique = set(words)
result = len(unique)
print(f"Total number of unique words:- {result}")