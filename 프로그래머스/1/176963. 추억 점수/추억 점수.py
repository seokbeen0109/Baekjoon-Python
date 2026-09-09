def solution(name, yearning, photo):
    answer = []
    
    for people in photo:            # 사진 하나씩 확인
        total = 0
        for person in people:        # 그 사진 속 인물 이름 하나씩 확인
            
            for i in range(len(name)):   # name 리스트를 처음부터 끝까지 뒤지면서
                if name[i] == person:     # 이름이 일치하면
                    total += yearning[i]   # 같은 위치(인덱스)의 점수를 더함
        
        answer.append(total)
    
    return answer