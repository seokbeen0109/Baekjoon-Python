def solution(k, score):
    answer = []
    temp = []
    for i in range(len(score)):        # k가 아니라 score의 실제 길이만큼 반복
        if len(temp) < k:
            temp.append(score[i])       # 아직 k개가 안 찼으면 그냥 추가
        elif score[i] > min(temp):      # k개가 다 찼고, 새 점수가 최소값보다 크면
            temp.remove(min(temp))       # 최소값 빼고
            temp.append(score[i])        # 새 점수 넣기
        answer.append(min(temp))         # (조건과 상관없이) 매번 현재 temp의 최소값 기록
    return answer