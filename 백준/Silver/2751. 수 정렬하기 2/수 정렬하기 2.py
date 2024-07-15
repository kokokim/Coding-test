import sys

n=int(input())
arr=[]
for i in range(n):
    arr.append(int(sys.stdin.readline().strip()))

s_arr=sorted(arr)

for i in s_arr:
    print(i)

