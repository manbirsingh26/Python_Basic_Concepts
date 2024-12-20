"""
daemon thread:- a thread that runs in the background, not important for program to run.
                our program will not wait for daemon threads to complete before exiting.
                non-daemon threads cannot normally be killed, they stay alive until the task is complete.
                uses e.g. background tasks, garbage collections, waiting for input, long running processes
"""
import threading
import time

def timer():
    print()
    count = 0
    while True:
        time.sleep(1)
        count += 1
        print(f"Logged in for {count} seconds")

#x = threading.Thread(target=timer, args=())  #simple non-daemon thread which will not killed
#Converting non-daemon thread into daemon thread
#Now the program will get exited right when we enter some input
x = threading.Thread(target=timer, daemon=True, args=())
print(x.daemon) #This checks if the thread is a daemon thread or not
x.start()
answer = input("Do you wish to exit?")  #This will be duty of main thread
