"""
dictionary_comprehension:- create dictionaries using an expression
                           can replace for loops and certain lambda function
Syntax:-
dictionary = {key:(value/expression) for key,value in iterable}
dictionary = {key:value for (key,value) in iterable if condition = true}
dictionary = {key:(if/else) for key,value in iterable}
dictionary = {key:(function/value) for key,value in iterable}
"""
#Example 1
#Expression
cities_temp_C = {
    "Jammu": 37,
    "New Delhi": 35,
    "Pune": 27,
    "Mumbai": 30,
    "Hyderabad": 25
}
cities_temp_F = {key: ((value * 9 / 5) + 32) for key, value in cities_temp_C.items()}
print(f"Relative temperatures of cities in Celsius are:-")
print(cities_temp_C)
print(f"Relative temperatures of cities in converted in Fahrenheit are:-")
print(cities_temp_F)

#Example 2
#Condition
cities_weather = {
    "Jammu": "Sunny",
    "New Delhi": "Sunny",
    "Pune": "Raining",
    "Mumbai": "Raining",
    "Hyderabad": "Windy",
    "Kashmir": "Snowing",
    "Kargil": "Snowing"
}
cities_weather_cond = {key: value for key, value in cities_weather.items() if value == "Sunny"}
print(f"Cities according to given condition:-")
print(cities_weather_cond)

#Example 3
#if/else
cities_temp = {
    "Jammu": 40,
    "New Delhi": 42,
    "Pune": 27,
    "Mumbai": 30,
    "Hyderabad": 25,
    "Nanded": 47
}
cities_desc = {key: ("Warm" if value >= 35 else "Cold") for key, value in cities_temp.items()}
print(f"Cities with their description of weathers:-")
print(cities_desc)

#Example_4
#Function
cities_tempe = {
    "Jammu": 40,
    "New Delhi": 47,
    "Pune": 27,
    "Mumbai": 30,
    "Hyderabad": 25,
    "Nanded": 47
}
def check_temp(value):
    if value >= 45:
        return "Warm"
    elif value >= 40:
        return "Hot"
    elif value >= 35:
        return "Mildly Hot"
    elif value < 35:
        return "Cool"
result = {key: check_temp(value) for key, value in cities_tempe.items()}
print(f"Result is:-")
print(result)




