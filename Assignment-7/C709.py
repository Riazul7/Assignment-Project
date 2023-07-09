import threading
def sum_of_square(start,end):
    result=sum([i**2 for i in range(start,end+1)])
    return result
results=[]
t1=threading.Thread(target=lambda:results.append(sum_of_square(1,2)))
t2=threading.Thread(target=lambda:results.append(sum_of_square(3,4)))
t3=threading.Thread(target=lambda:results.append(sum_of_square(5,6)))
t4=threading.Thread(target=lambda:results.append(sum_of_square(7,8)))
t5=threading.Thread(target=lambda:results.append(sum_of_square(9,10)))
t1.start()
t2.start()
t3.start()
t4.start()
t5.start()
print('The sum of squares of numbers from 1 to 10 is:',sum(results))