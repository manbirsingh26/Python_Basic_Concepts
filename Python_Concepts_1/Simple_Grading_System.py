"""
Grading System:
A: marks >= 90
B: marks >=80 and marks<90
C: marks >=70 and marks<80
D: marks >=60 and marks<70
E: marks <60
"""
print("***Grading System***")
marks = int(input("Enter your marks: "))
if 100 > marks >= 90:
    print("A grade")
elif 80 <= marks < 90:  # Instead of using and for comparison here, we can simply write it as one expression
    print("B grade")
elif marks >= 70 and marks < 80:
    print("C grade")
elif marks >= 60 and marks < 70:
    print("D grade")
elif marks < 60:
    print("E grade")
else:
    print("Invalid Input!!! ")
