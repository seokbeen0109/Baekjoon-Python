def solution(elements):
    answer = 0
    double=elements+elements
    n=len(elements)
    result=set()
    
    for i in range(1,n+1):
        dsum=sum(double[:i])
        result.add(dsum)
        for j in range(1,n):
            dsum+=double[j+i-1]-double[j-1]
            result.add(dsum)
    return len(result)