from collections import deque

def bfs(r,c):
    que=deque()
    que.append((r,c))
    visited[r][c] = True
    group=[(r,c)]
    
    dr=[-1, 1, 0, 0]
    dc=[0, 0, -1, 1]
    
    while que:
        r,c = que.popleft()
        # print("현재위치", r,c) #일단 들어왔어. 현재위치야. 이제 그 옆에 탐색하면서 차이가 나는 애들 group에 넣어.
         
        for i in range(4): #주변을 봐.
            nr=r+dr[i]
            nc=c+dc[i]
            
            if 0<=nr<N and 0<=nc<N : #그중에 방문도 안했고 차이도 조건에 맞아.
                if visited[nr][nc] == False: #방문을 안한 나라야. 그리고 그 나라와 지금 나라의 차이가 조건문을 만족하면 group에 넣어. 근데 일단 방문도해야해.
                    chai=abs(grid[r][c] - grid[nr][nc])
                    if L <=chai <= R:
                        # print("차이가 나는 국가", r,c,"랑", nr, nc)
                        visited[nr][nc] = True
                        group.append((nr,nc)) #일단 넣고 나중에 중복되는거 없애. set()으로.
                        que.append((nr, nc))
    return group
                    
N, L, R= map(int, input().split()) #땅크기, 조건1, 조건2
grid=[]
for _ in range(N):
    grid.append(list(map(int, input().split())))

day=0

dr=[-1, 1, 0, 0]
dc=[0, 0, -1, 1]

while True: #인구이동이 있으면 계속. 없으면 break
    visited=[[False]*N for _ in range(N)] #day마다 초기화되어야함.
    move=False
    for r in range(N):
        for c in range(N):
            if visited[r][c] == False:
                group=bfs(r,c)
                # print(len(group))
                # print(group)
                # print("원래 grid", grid)
                if len(group)>1 :
                    move=True
                    #이제 그 그룹안의 좌표들의 나라들의 인구이동 진행
                    sum=0
                    for i, j in group:
                        sum+=grid[i][j]
                    # print(sum)
                    sum=int(sum/len(group))
                    # print(sum)
                    for i, j in group:
                        grid[i][j] = sum
                    # print("바뀐 grid", grid)
    if move== False:
        break
    else:
        day+=1


print(day)
