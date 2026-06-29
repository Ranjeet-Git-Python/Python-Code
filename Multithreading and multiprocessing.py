'''Multithreading and multiprocessing are both ways to do multiple tasks in parallel, but they work differently.

Multithreading
Uses multiple threads inside one process.
Good for I/O-bound tasks like reading files, network requests, or waiting for input/output.
Threads share the same memory space.'''
#Example:

import threading
import time

def task():
    print("Task started")
    time.sleep(2)
    print("Task finished")

t1 = threading.Thread(target=task)
t2 = threading.Thread(target=task)

t1.start()
t2.start()

t1.join()
t2.join()

'''Multiprocessing
Uses multiple processes, each with its own memory space.
Good for CPU-bound tasks like heavy calculations, image processing, or data processing.
Safer for true parallelism because processes run independently.'''
#Example:
import multiprocessing
import time

def task():
    print("Task started")
    time.sleep(2)
    print("Task finished")

if __name__ == "__main__":
    p1 = multiprocessing.Process(target=task)
    p2 = multiprocessing.Process(target=task)

    p1.start()
    p2.start()

    p1.join()
    p2.join()

'''Main difference
Multithreading: better for I/O-bound work
Multiprocessing: better for CPU-bound work
Simple comparison
Thread = lighter, shares memory
Process = heavier, separate memory
If you want, I can also give you a small
real-world example using a CPU-heavy task like Fibonacci or a file download task.'''