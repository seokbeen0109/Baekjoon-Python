# https://www.acmicpc.net/problem/2512

import sys
input=sys.stdin.readline
n=int(input())
request=list(map(int, input().split()))
budget=int(input())

request.sort()
start=0
end=request[-1]
result=0

while start<=end:
    mid=(start+end)//2
    total=0
    for r in request:
         if r<=mid:
            total+=r
         else:
             total+=mid
    if total<=budget:
        result=mid
        start=mid+1
    else:
        end=mid-1
        
print(result)