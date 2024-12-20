import time
# finding epoch(a date and time from which a computer measures system time)
# epoch = when your computer thinks time began(reference point)
print(time.ctime(0)) # It converts a time expressed in seconds since epoch to a readable string
print(time.time()) # return current seconds since epoch

print(time.ctime(time.time())) # printing current date and time
# Another way to print current date and time
time_object_1 = time.localtime() # Local time
time_object_2 = time.gmtime()  #UTC(Coordinated Universal Time) time (by which world regulates clocks and time
print(time_object_1) # This will print complete structure of time object(time.struct_time())
print(time.strftime("%B %d %Y %H:%M:%S", time_object_1))
print(time.strftime("%B %d %Y %H:%M:%S", time_object_2))

#asctime()
#Takes a tuple representation of time as input and converts it into readable string
#(year, month, day, hours, minutes, secs, #day of the week, #day of the year, dst)
time_tuple = (2024, 10, 11, 8, 30, 0, 0, 0, 0)
print(time.asctime(time_tuple))

#mktime()
#Takes a tuple representation of time as input and converts it into seconds since epoch date
time_tuple = (2024, 10, 11, 8, 30, 0, 0, 0, 0)
print(time.mktime(time_tuple))






