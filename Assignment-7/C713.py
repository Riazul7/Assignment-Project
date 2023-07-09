import threading
import time
def send_message(user,message):
    print(f'{user}:{message}')
    time.sleep(0.5)
messages=['Hello!','Hi!','How are you?','I am fine.How are you?','I am fine.What are you doing now?','I am watching movies.What are you doing now?','I am doing a project.']
users=['Riazul','Pallab']
count=0
threads=[]
for message in messages:
    if count%2==0:
        t1=threading.Thread(target=send_message,args=(users[0],message))
        t1.start()
        threads.append(t1)
    else:
        t2=threading.Thread(target=send_message,args=(users[1],message))
        t2.start()
        threads.append(t2)
    count+=1
for thread in threads:
    thread.join()