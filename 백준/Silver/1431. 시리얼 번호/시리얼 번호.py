# https://www.acmicpc.net/problem/1431

def nsum(x):
    sum=0
    for i in x:
        if i.isdigit():
            sum+=int(i)
    return sum

n = int(input())
serial=[]
snum_sum=[]
for i in range(n):
    snum=input()
    serial.append(snum)

        
serial.sort(key=lambda x: (len(x), nsum(x), x))
for s in serial:
    print(s)