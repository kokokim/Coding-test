from collections import deque

def bfs(c,r):
    que = deque()
    que.append((r,c))
    
    dr=[-1, 1, 0, 0]
    dc=[0, 0, -1, 1]

    while que:
        r,c=que.popleft()
        
        for i in range(4):
            nr=r+dr[i]
            nc=c+dc[i]
            
            if 0<=nr<N and 0<=nc<M :
                if grid[nr][nc]==1:
                    if dist[nr][nc]==-1:
                        dist[nr][nc]=dist[r][c]+1
                        que.append((nr, nc))
                


N,M = map(int, input().split())
grid=[]
for _ in range(N):
    grid.append(list(map(int, input())))
dist=[[-1]*M for _ in range(N)]
dist[0][0]=1
bfs(0,0)

print(dist[N-1][M-1])