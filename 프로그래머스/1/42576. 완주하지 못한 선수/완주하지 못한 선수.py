# 선수 이름 participant
# 완주한 선수 completion

def solution(participant, completion):
    hash={}
    for p in participant:
        hash[p]=hash.get(p,0)+1
    for c in completion:
        hash[c]+=-1
    for key in hash:
        if hash[key]>0:
            return key
    answer = ''
    return answer