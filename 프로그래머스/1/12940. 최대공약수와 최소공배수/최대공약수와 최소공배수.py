def solution(n, m):
    answer = []
    temp=[]
    for i in range(1,min(n,m)+1):
        if n%i==0 and m%i==0:
            temp.append(i)
    gg=max(temp)
    answer.append(gg)
    answer.append((n*m)//gg)
    return answer