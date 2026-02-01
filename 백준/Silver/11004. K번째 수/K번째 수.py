# https://www.acmicpc.net/problem/11004

n,k = list(map(int, input().split()))

number=list(map(int, input().split()))
number.sort()
print(number[k-1])