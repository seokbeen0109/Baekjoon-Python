def solution(arr1, arr2):
    answer = []
    for i in range(len(arr1)):          # 행(row) 하나씩 꺼내기
        row = []
        for j in range(len(arr1[i])):    # 그 행 안의 열(col) 하나씩 꺼내기
            row.append(arr1[i][j] + arr2[i][j])  # 같은 위치끼리 더하기
        answer.append(row)               # 완성된 한 행을 결과에 추가
    return answer