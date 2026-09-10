def solution(s):
    count_transform = 0    # 이진 변환 횟수
    count_zero = 0          # 제거된 0의 총 개수
    
    while s != "1":
        count_transform += 1
        
        zero_count = s.count('0')   # 이번에 제거될 0의 개수
        count_zero += zero_count     # 총 0 개수에 누적
        
        s = s.replace('0', '')       # 0 전부 제거
        c = len(s)                    # 남은 1의 개수 (=x의 길이)
        s = bin(c)[2:]                # c를 2진법 문자열로 변환 ('0b' 제거)
    
    return [count_transform, count_zero]