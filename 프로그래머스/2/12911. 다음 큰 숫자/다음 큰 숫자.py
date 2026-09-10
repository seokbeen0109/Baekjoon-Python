def solution(n):
    target=bin(n).count('1')
    
    num=n+1
    while bin(num).count('1')!=target:
        num+=1
    return num