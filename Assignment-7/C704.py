import threading
def factorial(n):
    i=1
    if n == 0:
        print(f'The factorial of {n} is {i}')
    elif n>0:
        for j in range(1, n + 1):
            i = i * j
        print(f'The factorial of {n} is {i}')
    else:
        print('Factorial of this number is undefined.')
def user_input():
    n = int(input('Enter the number:'))
    t1=threading.Thread(target=factorial,args=(n,))
    t1.start()
t2=threading.Thread(target=user_input)
t2.start()