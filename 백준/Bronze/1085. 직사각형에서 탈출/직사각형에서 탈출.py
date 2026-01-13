# https://www.acmicpc.net/problem/1085

x,y,w,h=list(map(int, input().split()))

wx=w-x
hy=h-y
list1=[x,y,wx,hy]
list1.sort()
print(list1[0])

