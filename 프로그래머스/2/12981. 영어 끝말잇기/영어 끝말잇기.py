def solution(n, words):
    used=[words[0]]
    for i in range(1, len(words)):
        prev=words[i-1]
        cur=words[i]
        
        if cur[0] != prev[-1] or cur in used:
            person=i%n+1
            turn=i//n+1
            return [person, turn]
        used.append(cur)

    return [0,0]