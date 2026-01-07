# https://www.acmicpc.net/submit/2675

a=int(input())
for _ in range(a):
    num, word=input().split()
    for n in word:
        print(n*int(num),end="")
    print()