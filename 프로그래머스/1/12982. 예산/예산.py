def solution(d, budget):
    answer = 0
    d.sort()
    while(len(d)>0):
        if sum(d)>budget:
            d.pop()
        else:
            answer=len(d)
            break
    return answer