# https://www.acmicpc.net/problem/1110

N=int(input())
N_=N
cnt=0
while True:
    a=N//10 # a+b=c
    b=N%10
    c=(a+b)%10
    N=(b*10)+c
    
    cnt+=1
    
    if N==N_:
        break
    
print(cnt)