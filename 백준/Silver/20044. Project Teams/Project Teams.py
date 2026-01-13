# https://www.acmicpc.net/problem/20044

n=int(input())
n_2=list(map(int, input().split()))

n_2.sort()
a=[]

for i in range (0,n):
    a.append(n_2[i]+n_2[-(i+1)])

a.sort()
print(a[0])