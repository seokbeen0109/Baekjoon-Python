# https://www.acmicpc.net/problem/10818

a=int(input())
b=list(map(int, input().split()))

min=b[0]
max=b[0]

for i in b[1:]:
    if i>max:
        max=i
    elif i<min:
        min=i

print(min, max)