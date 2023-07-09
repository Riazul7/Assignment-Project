import threading
def display():
    print(f'{threading.current_thread().native_id}')
t1=threading.Thread(target=display)
t2=threading.Thread(target=display)
t3=threading.Thread(target=display)
t1.start()
t2.start()
t3.start()