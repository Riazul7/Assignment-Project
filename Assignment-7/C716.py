import threading
import time
import random
def read_sensor_data(sensor_name):
    for _ in range(4):
        data=random.randint(0,10)
        print(f'Data in {sensor_name}:{data}')
        time.sleep(0.5)
sensor_names=['sensor 1','sensor 2','sensor 3']
threads=[]
for sensor_name in sensor_names:
    thread=threading.Thread(target=read_sensor_data,args=(sensor_name,))
    threads.append(thread)
    thread.start()
for thread in threads:
    thread.join()