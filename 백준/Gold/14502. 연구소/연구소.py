from collections import deque
import sys
import copy
sys.setrecursionlimit(10000)

N, M = map(int, input().split())
grid=[]
for _ in range(N):
    grid.append(list(map(int, input().split())))

zeros = []
for r in range(N):
    for c in range(M):
        if grid[r][c] ==0 :
            zeros.append((r,c))

from itertools import combinations
empty=[]
cnt=0
for room in combinations(zeros, 3):
    empty.append(room)
    cnt+=1
    
max_saferoom=0

def bfs(r,c):    
    que=deque()
    que.append((r,c))
    visited[r][c] = True
    
    dr=[-1, 1, 0, 0]
    dc=[0, 0, -1, 1]
    
    while que:
        r,c = que.popleft() # 애는 지금 바이러스 2

        
        for i in range(4):
            nr=r+dr[i]
            nc=c+dc[i]
            
            if 0<=nr<N and 0<=nc<M : 
                if visited[nr][nc] == False and grid_copy[nr][nc] != 1 : 
                    visited[nr][nc] = True 

                    grid_copy[nr][nc] = 2
                    que.append((nr, nc))

for i in range(cnt): 

    for j in range(3):
        r,c = empty[i][j]
        grid[r][c] = 1 

    grid_copy = copy.deepcopy(grid)
    visited=[[False]*M for _ in range(N)]

    for a in range(N):
        for b in range(M):
            if grid_copy[a][b] == 2 and visited[a][b]==False:

                bfs(a,b)

    saferoom = 0
    for aa in range(N):
        for bb in range(M):
            if grid_copy[aa][bb] == 0:
                saferoom+=1

    max_saferoom = max(saferoom, max_saferoom)

    for jj in range(3):
        rr,cc = empty[i][jj]
        grid[rr][cc] = 0

print(max_saferoom)