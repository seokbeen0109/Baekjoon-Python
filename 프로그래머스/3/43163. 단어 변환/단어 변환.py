from collections import deque
def solution(begin, target, words):
    if target not in words:
        return 0
    
    queue=deque()
    queue.append((begin,0))
    visited=set()
    visited.add(begin)
    
    while queue:
        word,step=queue.popleft()
        if word==target:
            return step
        for w in words:
            if w not in visited and diff_one(word,w):
                visited.add(w)
                queue.append((w,step+1))
    return 0

def diff_one(a,b):
    count=0
    for i in range(len(a)):
        if a[i]!=b[i]:
            count+=1
    return count ==1