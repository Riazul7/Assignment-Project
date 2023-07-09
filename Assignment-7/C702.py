import threading
def even_sum():
    print(sum([num for num in range(0,101,2)]))
t1=threading.Thread(target=even_sum)
t1.start()