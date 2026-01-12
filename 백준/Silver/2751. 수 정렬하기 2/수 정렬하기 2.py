# https://www.acmicpc.net/problem/2751lines=int(input())
import sys
lines = int(sys.stdin.readline())
a = []

for _ in range(lines):
    a.append(int(sys.stdin.readline()))

a.sort()

for i in a:
    print(i)