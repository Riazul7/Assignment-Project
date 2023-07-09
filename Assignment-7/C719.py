import threading
def is_prime(n):
    for i in range(2, int(n / 2) + 1):
        if n % i == 0:
            return False
    else:
        return True
def sum_of_prime():
    l = []
    number = int(input('Enter number upto which sum of prime number needs to be calculated:'))
    for n in range(2, number + 1):
        if is_prime(n):
            l.append(n)
    print(sum(l))
t1=threading.Thread(target=sum_of_prime)
t1.start()
t1.join()