import api_queue


def test_api_queue():
    q = api_queue.queue.Queue()
    TOTAL_THREADS = 5

    # Turn-on the worker threads.
    for thread in range(TOTAL_THREADS):
        api_queue.threading.Thread(target=api_queue.worker, daemon=True).start()

    for item in range(1):
        # Put a bunch of sleep tasks with different sleep time parameters
        q.put((api_queue.sleep, 1))

    # Block until all tasks are done.
    q.join()

    assert q.empty()

