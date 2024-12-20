Student1 = dict(Name="Manbir", Class="B.E", RollNo=19, CGPA=8.42)
Student2 = dict(Name="Harleen", Class="B.E", RollNo=20, CGPA=7.85)
Student3 = {
    "Name": "Ranjodh",
    "Class": "B.E",
    "RollNo": 18,
    "CGPA": 7.82
}
def output():
    a = Student1["CGPA"]
    b = Student2["CGPA"]
    c = Student3["CGPA"]
    if b < a > c:
        print("Name of topper is", Student1["Name"], "with CGPA of", Student1["CGPA"])
    elif a < b > c:
        print("Name of topper is:", Student2["Name"], "with CGPA of ", Student2["CGPA"])
    elif a < c > b:
        print("Name of topper is:", Student3["Name"], "with CGPA of ", Student3["CGPA"])

