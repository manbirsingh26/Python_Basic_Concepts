"""
Given a list of marks of students. Print the following details for topper student:-
1. Name
2. Marks
"""
marks = {"Manbir": 450, "Harleen": 452, "Avneet": 445, "Ranjodh": 421, "Manan": 441, "Paman": 433}
marks_list = list(marks.values())
# we can also use traditional approach instead of max method to find largest in the list
"""
high = 0
for i in marks-list:
    if i > high:
         high = i
print(high)         
"""
for key, value in marks.items():
    if value == max(marks_list):
        print("Name of topper student:-", key)
        print("Marks of student:-", max(marks_list))
