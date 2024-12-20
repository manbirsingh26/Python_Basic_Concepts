"""
Write a program to take date and time as input from user and display them in the following format:-
day/month/year hour(s):minutes:seconds
"""
import datetime as dt
date_time = input("Enter date and time (in the format: YYYY-MM-DD HH:MM:SS):- ")
result = dt.datetime.strptime(date_time, "%Y-%m-%d %H:%M:%S")
result_desired = result.strftime("%d/%m/%Y %H:%M:%S")
print(f"Entered date and time is:- {result_desired}")
