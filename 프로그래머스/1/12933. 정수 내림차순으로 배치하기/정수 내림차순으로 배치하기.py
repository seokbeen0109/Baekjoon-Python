def solution(n):
    answer = ""
    n=str(n)
    n=list(n)
    n.sort()
    n.reverse()
    for num in n:
        answer+=num
    return int(answer)