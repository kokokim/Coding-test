from collections import deque

def bfs(r,c):
    que=deque()
    que.append((r,c))
    visited[r][c] = True
    
    while que:
        r,c = que.popleft() #미세먼지 있는 좌표
        # print()
        # print("현재위치", r,c,)
        hs=int(grid[r][c]/5) #현재 좌표에서 확산될 양
        # print("현재위치에서 확산될 양", hs)
        count=0
         
        for i in range(4): #주변으로 4방향 보고
            nr=r+dr[i]
            nc=c+dc[i]
            
            if 0<=nr<N and 0<=nc<M: #벽이 아니라 방이라면
                if grid[nr][nc] !=-1: #공기청정기도 아니라면,
                    # print("후보위치", nr, nc)
                    count+=1
                    # if visited[nr][nc] == False: #그리고 아직 방문 안했다면
                        # visited[nr][nc] = True #일단 방문해
                        
                    grid2[nr][nc] +=hs #일단 벽이 아니라 칸이면 확산해. 공기청정기도 안돼.
                        # print("다음위치", nr,nc)
                        # que.append((nr, nc))
        # print(count)
        if count>=1: #주변에 확산될 칸 개수만큼 현재위치에서도 변화량 계산
            a=-(hs*count)
            # print("현재위치에서 계산될 변화량", a)
            grid2[r][c] +=(-(hs*count))
            # print("grid2", grid2)
    return grid2
    
def move(r):
    #왼->오
    for j in range(1, M-1): #1, 2, 3, 4, 5
        # print("j는", j, end=" ")
        grid3[r][j+1] = grid[r][j]
    # print("왼오",grid3)
    #오->위쪽
    for i in range(r, 0, -1): #2 1
        # print("i는", i, end=" ")
        grid3[i-1][M-1] = grid[i][M-1]
    # print("오위", grid3)

    #오->왼
    for j in range(M-1, 0, -1): #6 5 4 3 2 1
        # print("j는", j, end=" ")
        grid3[0][j-1] = grid[0][j]
    #왼->밑쪽
    for i in range(r-1): #0
        # print("i는", i, end=" ")
        grid3[i+1][0] = grid[i][0]
    
def move2(r):
    #왼 ->오
    for j in range(1, M-1): #1, 2, 3, 4, 5
        # print("j는", j)
        grid3[r][j+1] = grid[r][j]
    #오->밑쪽
    for i in range(r, N-1): #3 4 5
        # print("i는", i, end=" ")
        grid3[i+1][M-1] = grid[i][M-1]
    #밑쪽 -> 왼
    for j in range(M-1, 0, -1): #6 5 4 3 2 1
        # print("j는", j, end=" ")
        grid3[N-1][j-1] = grid[N-1][j]
    #왼 -> 위쪽
    for i in range(N-1, r+1, -1): #6 5
        # print("i는", i, end=" ")
        grid3[i-1][0] = grid[i][0]
        
        
    
N, M, T = map(int, input().split())
grid=[]
for _ in range(N):
    grid.append((list(map(int, input().split())))) 
    

#시계방향
dr=[-1, 0, 1, 0]
dc=[0, 1, 0, -1]
total_mise=0
chung=[]

#일단 공기청소기나 찾아
for i in range(N):
    for j in range(M):
        if grid[i][j] == -1:
            chung.append((i,j))

for i in range(T):
    visited=[[False]*M for _ in range(N)]
    grid2=[[0]*M for _ in range(N)]
    grid3=[[0]*M for _ in range(N)]
    
    for r in range(N):
        for c in range(M): #완전탐색으로 일단 미세먼지 있는 좌표로 가
            #미세먼지 확산
            if visited[r][c] == False and grid[r][c]!=0 and grid[r][c]!=-1:
                # print("확산전", grid)
                grid2=bfs(r,c)
                
    # print("확산window", grid2) #잘 확산되었는지 확인
    for i in range(N):
        for j in range(M):
            grid[i][j] = grid[i][j]+grid2[i][j]
    # print("되나?", grid)
    
    #이제 공기청정기 작동 -> 알고리즘은 필요 x 걍 방향키도 안돼. 더 복잡해
    #테두리를 따라 값들을 한칸씩 땡긴다.
    move(chung[0][0])
    move2(chung[1][0])
    # print("으아", grid3)
    grid3[chung[0][0]][0] = -1
    grid3[chung[1][0]][0] = -1
    
    for i in range(1, chung[0][0]):
        for j in range(1, M-1):
            grid3[i][j] = grid[i][j]
    
    for i in range(chung[1][0]+1, N-1):
        for j in range(1, M-1):
            grid3[i][j] = grid[i][j]
    grid=grid3

#출력은 미세먼지 양 출력
for i in range(N):
    for j in range(M):
        if grid[i][j]!= -1:
            total_mise+=grid[i][j]
print(total_mise)