import threading
import queue
import time
from time import sleep

# Initialize Queue
q = queue.Queue()

# Set the total number of concurrent threads allowed
TOTAL_THREADS = 5


def worker():
    while True:
        # Get name of thread
        thread_name = threading.current_thread().name

        # Pop tuple off the queue where first element is a function and second element has the parameter
        item = q.get()
        function = item[0]
        parameter = item[1]
        curr_time = time.localtime()
        print(f'{thread_name} started working on {function} at {curr_time[3]}:{curr_time[4]}:{curr_time[5]}')
        function(parameter)
        curr_time = time.localtime()
        print(f'{thread_name} finished {function} at {curr_time[3]}:{curr_time[4]}:{curr_time[5]}')
        q.task_done()


# Turn-on the worker threads.
for thread in range(TOTAL_THREADS):
    threading.Thread(target=worker, daemon=True).start()


# Send thirty task requests to the worker.
for item in range(30):
    q.put((sleep, 5))

# Block until all tasks are done.
q.join()

print('All work completed')
