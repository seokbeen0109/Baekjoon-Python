# https://www.acmicpc.net/problem/2587
import sys
input=sys.stdin.readline
num=[]
for _ in range(5):
    number=int(input())
    num.append(number)

num.sort()
print(int(sum(num)/len(num)))
print(num[2])