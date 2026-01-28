# https://www.acmicpc.net/problem/2606
n=int(input()) # 컴퓨터의 수
m=int(input()) # 연결된 컴퓨터 쌍 수 (간선의 수)
count=0
def dfs(graph,v,visited):
    global count
    visited[v]=True
    

    for i in graph[v]:
        if not visited[i]:
            dfs(graph,i,visited)
            count+=1


graph = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(1, n + 1): # 번호가 낮은 노드부터 방문하도록 sort
    graph[i].sort()

visited_dfs=[False]*(n+1)
dfs(graph,1,visited_dfs)
print(count)