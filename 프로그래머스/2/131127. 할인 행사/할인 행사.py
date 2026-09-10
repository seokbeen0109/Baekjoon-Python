def solution(want, number, discount):
    from collections import Counter
    answer = 0
    wanted=dict(zip(want,number))
    
    for start in range(len(discount)-9):
        period=discount[start:start+10]
        period_count=Counter(period)
        
        if period_count == wanted:
            answer+=1
    return answer