# https://www.acmicpc.net/problem/18353

import sys
input=sys.stdin.readline
a=int(input())
ai=list(map(int, input().split()))
d=[1]*a

for i in range(a):
    for j in range(i):
        if ai[j]>ai[i]:
            d[i]=max(d[i],d[j]+1)

print(a-max(d))