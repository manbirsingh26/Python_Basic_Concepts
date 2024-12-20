"""
########################
Python Multiprocessing
########################
Multiprocessing:- running tasks in parallel on different CPU cores, bypasses GIL used for threading
                  multiprocessing = better for CPU bound tasks (heavy CPU usage)
                  multithreading  = better for I/O bound tasks (waiting around)
"""
from multiprocessing import Process, cpu_count
import time

def counter(num):
    count = 0
    while count < num:
        count += 1


def main():
    print("CPU count:", cpu_count()) #It counts that how many CPU cores our pc has
    #a = Process(target=counter, args=(10000000,))
    # Multiprocessing (by dividing the a task among different processes)
    a = Process(target=counter, args=(50000000,))
    b = Process(target=counter, args=(50000000,))
    a.start()
    b.start()
    #Process synchronization with same syntax as thread synchronization
    a.join()
    b.join()
    # This will print how many seconds will main thread take to count from 0 to num
    # We can speed this up using multiprocessing
    print("Finished in:", time.perf_counter(), "seconds.")


if __name__ == "__main__":
    main()
