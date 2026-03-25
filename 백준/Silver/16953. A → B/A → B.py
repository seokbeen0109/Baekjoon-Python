# https://www.acmicpc.net/problem/16953

import sys
input=sys.stdin.readline

a,b=map(int, input().split())
count=1
while(a<b):
    if b%2==0:
        b=b//2
    elif b%10==1:
        b=b//10
    else:
        break
    count+=1
    
if a==b:
    print(count)
else:
    print(-1)