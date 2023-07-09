import threading
import time
class ProducerConsumer:
    def __init__(self):
        self.buffer=[]
    def producer(self,rlock):
        self.produce_item = 1
        while True:
            time.sleep(1)
            rlock.acquire()
            if len(self.buffer) < 10:
                self.buffer.append(self.produce_item)
                print(f'Producer produces item {self.produce_item}')
                self.produce_item += 1
            rlock.release()
    def consumer(self,rlock):
        while True:
            rlock.acquire()
            if len(self.buffer)>0:
                self.consume_item=self.buffer.pop(0)
                print(f'Consumer consumes item {self.consume_item}')
                rlock.release()
            else:
                rlock.release()
                time.sleep(1)
producer_consumer=ProducerConsumer()
rlock=threading.RLock()
t1=threading.Thread(target=producer_consumer.producer,args=(rlock,))
t2=threading.Thread(target=producer_consumer.consumer,args=(rlock,))
t1.start()
t2.start()