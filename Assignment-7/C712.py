import threading
import os
def file_size_func(file):
    print(f'The size of {os.path.basename(file)} file is {os.path.getsize(file)} bytes.')
file_list=['fileone.txt','filetwo.txt','myfile.txt']
threads=[]
for file in file_list:
    thread=threading.Thread(target=file_size_func,args=(file,))
    thread.start()
    threads.append(thread)
for thread in threads:
    thread.join()