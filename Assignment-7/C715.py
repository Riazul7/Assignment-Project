import threading
def search(target_number,number_list,result):
    if target_number in number_list:
        result.append(target_number)
number_list=input('Enter numbers in list separated by space:')
target_number=float(input('Enter target number:'))
l=[]
for number in number_list.split():
    number=int(number)
    l.append(number)
mid=len(l)//2
left=l[:mid]
right=l[mid:]
result=[]
if len(number_list)==1:
    t1=threading.Thread(target=search,args=(target_number,l,result))
    t1.start()
    if len(result)>0:
        print(f'{result[0]} is found.')
    else:
        print(f'Target number is not found.')
    t1.join()
else:
    t2=threading.Thread(target=search,args=(target_number,left,result))
    t3=threading.Thread(target=search,args=(target_number,right,result))
    t2.start()
    t3.start()
    if len(result)>0:
        print(f'{result[0]} is found.')
    else:
        print(f'Target number is not found.')
    t2.join()
    t3.join()