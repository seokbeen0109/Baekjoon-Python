def solution(k, tangerine):
    from collections import Counter
    count=Counter(tangerine)
    sort_count=sorted(count.values(), reverse=True)
    
    answer = 0
    total=0
    for num in sort_count:
        if total>=k:
            break
        total+=num
        answer+=1
    return answer