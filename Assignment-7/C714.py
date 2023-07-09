import threading
import time
def display(rlock):
    rlock.acquire()
    for count in range(1,11):
        time.sleep(0.5)
        print(count)
    rlock.release()
threads=[]
rlock=threading.RLock()
for _ in range(3):
    thread=threading.Thread(target=display,args=(rlock,))
    thread.start()
    threads.append(thread)
for thread in threads:
    thread.join()