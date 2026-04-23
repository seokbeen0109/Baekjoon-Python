# N 마리 중 N/2 마리 가져갈 수 있음
# [3,1,2,3] 주어지면
# 3,1 / 3,2 / 3,3 / 1,2 / 1,3 / 2,3

def solution(nums):
    go=len(nums)//2
    unique=len(set(nums))
    answer = min(go,unique)
    return answer