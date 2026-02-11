# https://www.acmicpc.net/problem/7795

import sys
input=sys.stdin.readline
t=int(input()) # 테스트 케이스 개수

def binary(start, end, target, bb):
    while start<=end:
        mid=(start+end)//2
        if bb[mid]>=target:
            end=mid-1
        else:
            start=mid+1
    return start

for _ in range(t):
    a,b=list(map(int,input().split()))
    an=list(map(int,input().split()))
    bn=list(map(int,input().split()))
    bn.sort()
    count=0
    for aa in an:
        if aa<=bn[0]:
            continue
        else:
            count+=binary(0,len(bn)-1,aa,bn)
    print(count)