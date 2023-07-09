import concurrent.futures
import time
def task1():
    print('Sleeping 3 seconds...')
    time.sleep(3)
    print('Done sleeping 3 seconds...')
def task2():
    print('Sleeping 2 seconds...')
    time.sleep(2)
    print('Done sleeping 2 seconds...')
def task3():
    print('Sleeping 0.5 seconds...')
    time.sleep(0.5)
    print('Done sleeping 0.5 seconds...')
with concurrent.futures.ThreadPoolExecutor() as executor:
    tasks=[task1,task2,task3]
    results=[executor.submit(task) for task in tasks]
    for f in concurrent.futures.as_completed(results):
        f.result()