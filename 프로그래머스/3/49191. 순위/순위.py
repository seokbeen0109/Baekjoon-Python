from collections import deque
def solution(n, results):
    win=[[False]*(n+1) for _ in range(n+1)]
    
    for a,b in results:
        win[a][b]=True
        
    for i in range(1, n+1):
        for j in range(1, n+1):
            for k in range(1, n+1):
                if win[j][i] and win[i][k]:
                    win[j][k]=True
                    
    answer=0
    for i in range(1, n+1):
        count=0
        for j in range(1, n+1):
            if i!=j and (win[i][j]or win[j][i]):
                count+=1
        if count==n-1:
            answer+=1
        
    return answer