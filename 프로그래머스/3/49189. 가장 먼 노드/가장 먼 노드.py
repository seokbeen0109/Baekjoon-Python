from collections import deque

def solution(n, vertex):
    graph=[[] for _ in range(n+1)]
    for a, b in vertex:
        graph[a].append(b)
        graph[b].append(a)
        
    distance=[-1]*(n+1)
    distance[1]=0
    
    queue=deque()
    queue.append(1)
    
    while queue:
        node=queue.popleft()
        for next_node in graph[node]:
            if distance[next_node]==-1:
                distance[next_node]=distance[node]+1
                queue.append(next_node)
                
    max_dist=max(distance[1:])
    return distance[1:].count(max_dist)