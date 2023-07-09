import threading
import time
x=100
def addition(num,lock):
    global x
    with lock:
        x+=num
        time.sleep(.5)
        print(f'After addition x is {x}')
def subtraction(num,lock):
    global x
    with lock:
        x-=num
        time.sleep(.5)
        print(f'After subtraction x is {x}')
lock=threading.Lock()
t1=threading.Thread(target=addition,args=(10,lock))
t2=threading.Thread(target=subtraction,args=(25,lock))
t1.start()
t2.start()