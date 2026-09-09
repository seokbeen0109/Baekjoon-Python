def solution(x, n):
    answer = []
    x_1=x
    while(n>0):
        
        answer.append(x_1)
        x_1+=x
        n-=1
    return answer