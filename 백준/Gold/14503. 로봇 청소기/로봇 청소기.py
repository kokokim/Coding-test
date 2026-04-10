from collections import deque
import sys
sys.setrecursionlimit(100000)
import copy
from itertools import combinations, permutations

N, M = map(int, input().split())
r,c,d=map(int, input().split())
grid=[]
for _ in range(N):
    grid.append(list(map(int, input().split())))

cnt=0
chungso=[[False]*M for _ in range(N)]       


def robot(r,c,d):
    while True:
        #현재 위치 일단 청소해
        if chungso[r][c] == False:
            chungso[r][c] = True
        # print("현재위치", r,c)
        
        
        # dr=[-1, 1, 0, 0]
        # dc=[0, 0, -1, 1]
        
        dr=[-1, 0, 1, 0]
        dc=[0, 1, 0, -1]
        moved=False
        
        for i in range(4):
            d=(d-1)%4   
            nr=r+dr[d]
            nc=c+dc[d]
            # print("다음위치", nr, nc)
    
            if grid[nr][nc] ==0 and chungso[nr][nc] == False:
                if 0<=nr<N and 0<=nc<M : 
                    r,c = nr, nc
                    # print("청소안된곳 옮겨가자", nr, nc)
                    moved = True
                    break
                
        if moved==False:
            back = (d+2)%4
            nr=r+dr[back]
            nc=c+dc[back]
            if grid[nr][nc] == 1:
                break
            else:
                r,c = nr,nc


  
robot(r,c,d)

for i in range(N):
    for j in range(M):
        if chungso[i][j] == True:
            cnt+=1
print(cnt)