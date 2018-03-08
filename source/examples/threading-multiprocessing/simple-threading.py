
import threading
import time
import random


def func():
    for i in range(5):
        print("hello from thread %s" % threading.current_thread().name)
        time.sleep(random.random() * 2)


threads = []
for i in range(3):
    thread = threading.Thread(target=func, args=())
    thread.start()
    threads.append(thread)

for thread in threads:
    thread.join()
