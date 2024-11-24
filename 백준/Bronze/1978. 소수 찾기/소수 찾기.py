n=int(input())
arr=list(map(int, input().split()))

s=True
num=0
for i in arr:
    if i==1:
        continue
    for j in range(2, i):
        if i%j==0:
            s=False
    if s==True:
        num+=1
    s=True

print(num)