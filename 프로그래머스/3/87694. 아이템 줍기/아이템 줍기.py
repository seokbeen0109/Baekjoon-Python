from collections import deque
def solution(rectangle, characterX, characterY, itemX, itemY):
    board=[[0]*103 for _ in range(103)]
    
    for x1,y1, x2, y2 in rectangle:
        x1,y1,x2,y2=x1*2,y1*2,x2*2,y2*2
        for x in range(x1, x2+1):
            for y in range(y1,y2+1):
                board[x][y]=1
                
    for x1,y1, x2, y2 in rectangle:
        x1,y1,x2,y2=x1*2,y1*2,x2*2,y2*2
        for x in range(x1+1,x2):
            for y in range(y1+1,y2):
                board[x][y]=0
                
    sx,sy=characterX*2, characterY*2
    ex, ey=itemX*2, itemY*2
    
    visited=[[False]*103 for _ in range(103)]
    queue=deque()
    queue.append((sx,sy,0))
    visited[sx][sy]=True
    dx=[-1,1,0,0]
    dy=[0,0,-1,1]
    
    while queue:
        x,y,dist=queue.popleft()
        if x==ex and y==ey:
            return dist//2
        
        for i in range(4):
            nx,ny=x+dx[i], y+dy[i]
            if 0<=nx<103 and 0<=ny<103:
                if board[nx][ny]==1 and not visited[nx][ny]:
                    visited[nx][ny]=True
                    queue.append((nx,ny,dist+1))
    
    return -1