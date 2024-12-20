"""
thread:- a flow of execution. Like a separate order of instructions that a program can follow.
         However each thread takes a turn running to achieve concurrency due to
         GIL = (global interpreter lock) which only allows only one thread to hold the control
         of the Python Interpreter at any one time.
Two types of tasks:-
1.cpu bound = program/task spends most of its time waiting for internal events(e.g CPU intensive)
Better to use multiprocessing for CPU bound tasks

2.io bound = program/task spends most of its time waiting for external events(e.g user input, web scrapping)
Better to use multithreading for io bound tasks
"""
import threading
import time
start_time = time.perf_counter()

def eat_breakfast():
    time.sleep(5)
    print(f"You ate breakfast")

def drink_coffee():
    time.sleep(6)
    print(f"You drank coffee")

def study():
    time.sleep(7)
    print(f"You studied")

#Multithreading:- creating multiple threads for different tasks so that load isn't  on main thread and can be
#divided
x = threading.Thread(target=eat_breakfast, args=())
x.start()
y = threading.Thread(target=drink_coffee, args=())
y.start()
z = threading.Thread(target=study, args=())
z.start()

#thread synchronization
# Here the "main thread" has to wait for other threads to finish before it can move on
# with its own set of instructions
#Here the active_count of threads will be 1 at the end instead of 4 because these threads will finish before
#the main thread will have started
#x.join()
#y.join()
#z.join()

#eat_breakfast()
#drink_coffee()
#study()

# active_count(): it counts the number of threads running currently
print(threading.active_count())

# enumerate(): It can be used to list the names of all active threads
print(threading.enumerate())

# time.perf_counter(): It counts how many seconds "main thread" take to complete the set of instructions
# however it returns a very large value if we use it directly, so we take difference of starting and ending time
end_time = time.perf_counter()
res = end_time - start_time
print(res)







