def solution(order):
    answer = 0
    if "3" or "6" or "9" in str(order):
        answer+=str(order).count("3")
        answer+=str(order).count("6")
        answer+=str(order).count("9")
    return answer