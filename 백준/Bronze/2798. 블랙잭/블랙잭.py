# https://www.acmicpc.net/problem/2798

n,m=list(map(int, input().split()))

numbers=list(map(int, input().split()))

numbers.sort()
sum=0

for i in range(n):
    for j in range(i+1, n):
        for k in range(j+1, n):
            if numbers[i]+numbers[j]+numbers[k]>m:
                continue
            else:
                sum=max(sum, (numbers[i]+numbers[j]+numbers[k]))
print(sum)