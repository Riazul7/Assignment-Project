#Q2:You are given a list of integers. Write a program that finds the longest subsequence of consecutive numbers in the list. A subsequence is considered consecutive if the numbers are in increasing order without any gaps. The program should output the length of the longest consecutive subsequence.
l=[1,2,3,5,6,7,8,12,11,10,51,52,53,54,55,56]
r=0
for n in l:
    count=1
    if n-1 not in l:
        while n+1 in l:
              count+=1
              n+=1
        r=max(r,count)
print(r)