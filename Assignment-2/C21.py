#Q1:Write a program that reads a text file containing a list of numbers, and outputs the sum of all the even numbers in the list. The program should ignore any non-numeric entries in the file.
f=open("D:\\txt.txt","r")
f1=str(f.read())
# print(f1)
n=[int(i) for i in f1.split() if i.isdigit()]
# print(n)
l=[]
for i in n:
    if i%2==0:
        l.append(i)
print(sum(l))