# Different ways to create a thread:
# 1. without class:
from threading import Thread
def display():
    for i in range(1, 11):
        print("Child Thread")
t = Thread(target=display)
t.start()
for i in range(1,11):
    print("Main Thread")

# 2. with class:
from threading import Thread

class Mythread(Thread):
    def run(self):
        for i in range(1, 11):
            print("Child Thread")
t = Mythread()
t.start()
for i in range(1,11):
    print("Main Thread")
    
# 3. without threading:
import time
numbers = [1,2,3,4,5]

def double_numbers(numbers):
    for n in numbers:
        print("Doubles", 2 * n)

def square_numbers(numbers):
    for n in numbers:
        print("Squares", n * n)

begin_time = time.time()
double_numbers(numbers)
square_numbers(numbers)
end_time = time.time()

print(f"Time taken:, {end_time-begin_time}")   

# 4. with threading:
import threading
import time

numbers = [1,2,3,4,5]

def double_numbers(numbers):
    for n in numbers:
        print("Doubles", 2 * n)

def square_numbers(numbers):
    for n in numbers:
        print("Squares", n * n)

begin_time = time.time()
thread1 = threading.Thread(target=double_numbers, args=(numbers, ))
thread2 = threading.Thread(target=square_numbers, args=(numbers, ))

thread1.start()
thread2.start()

thread1.join()
thread2.join()

end_time = time.time()

print(f"Time taken:, {end_time-begin_time}")
