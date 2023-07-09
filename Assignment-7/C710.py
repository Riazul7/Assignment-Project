import threading
import time
def sleep_func():
    time.sleep(.5)
number_of_thread=int(input('Enter the number of threads:'))
func=input('Enter the function:')
if func=='sleep_func':
    func=eval(func)
    start=time.time()
    threads=[]
    for _ in range(number_of_thread):
        thread=threading.Thread(target=func)
        thread.start()
        threads.append(thread)
    for thread in threads:
        thread.join()
    end=time.time()
    print(f'Execution time of a function using threading is {end-start}')
else:
    print('The function is not defined here!')