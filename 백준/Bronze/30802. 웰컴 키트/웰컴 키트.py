# https://www.acmicpc.net/problem/30802

n=int(input())

size=list(map(int, input().split()))

shirts, pen = map(int, input().split())

s_count=0

for i in size:
    if i==0:
        continue
    elif i<=shirts:
        s_count+=1
    elif i%shirts==0:
        s_count+=i//shirts
    else :
        s_count+=(i//shirts)+1

print(s_count)
print(n//pen, n%pen)

