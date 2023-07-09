import threading
import time
def green_light(pattern,rlock):
    rlock.acquire()
    if pattern==0:
        print('Green light-Go!')
        time.sleep(1)
    rlock.release()
def yellow_light(pattern,rlock):
    rlock.acquire()
    if pattern==1:
        print('Yellow light-Prepare to stop!')
        time.sleep(1)
    rlock.release()
def red_light(pattern,rlock):
    rlock.acquire()
    if pattern==2:
        print('Red light-Stop!')
        time.sleep(1)
    rlock.release()
patterns=[0,1,2]
rlock=threading.RLock()
for pattern in patterns:
    t1=threading.Thread(target=green_light,args=(pattern,rlock))
    t2=threading.Thread(target=yellow_light,args=(pattern,rlock))
    t3=threading.Thread(target=red_light,args=(pattern,rlock))
    t1.start()
    t2.start()
    t3.start()
    t1.join()
    t2.join()
    t3.join()