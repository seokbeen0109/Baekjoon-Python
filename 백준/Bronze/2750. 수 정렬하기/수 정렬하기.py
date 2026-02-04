# https://www.acmicpc.net/problem/2750
import sys
input=sys.stdin.readline
N=int(input())
num=[]
for _ in range(N):
    number=int(input())
    num.append(number)

num.sort()
for n in num:
    print(n)