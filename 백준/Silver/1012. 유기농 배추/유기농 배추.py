from collections import deque
import sys
sys.setrecursionlimit(1000000)

def dfs(r,c):
    visited[r][c] = True
    
    dr=[-1, 1, 0, 0]
    dc=[0, 0, -1, 1]
    
    for i in range(4):
        nr=r+dr[i]
        nc=c+dc[i]
        
        if 0<=nr<N and 0<=nc<M :
            if grid[nr][nc]==1 and visited[nr][nc] == False:
                dfs(nr, nc)
                        

T = int(input())

for i in range(T):
    count = 0
    M, N, K = map(int, input().split())
    grid=[[0]*M for _ in range(N)]

    for _ in range(K):
        c,r = map(int, input().split())
        grid[r][c] = 1
        
    visited=[[False]*M for _ in range(N)]

    for i in range(N):
        for j in range(M):
            if grid[i][j] == 1 and visited[i][j]==False:
                count+=1
                dfs(i,j)
    
            
    print(count)