"""
Default Arguments
Syntax:- non-default argument comes before default argument
def func_name(non-default, default):
And if we write default argument first and non-default after, then error is generated
"""
def info(name, hobby="running"):   #Here running is a default value(argument) passed to hobby
    print(f"My name is {name} and my hobby is {hobby}")
    return 0
info("Manbir")  #Here it will print default value of hobby i.e running
info("Manbir", "cycling")  #Here it will print updated value of hobby

"""
Keyword Arguments
Stores data in a dictionary format
Syntax:- 
**kwargs
"""
def keyword(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}:{value}")
    return 0
keyword(Name="Manbir", Address="Jammu", Hobby=["Cycling", "Meditation"], Position="Data Analyst")
keyword(Name="Harleen", Address="RS Pura", Hobby=["Running", "Driving"], Position="Front-End Developer")



