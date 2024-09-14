# @는 3을 곱하고 %는 5를 더하며 #는 7을 빼라는 연산자

T=int(input())
line=[]

for i in range(T):
    l=map(str, input().split())
    line.append(list(l))
    
for i in line:
    sum=0
    for j in i:
        if j=='@':
            sum*=3
            continue
        elif j=='%':
            sum+=5
            continue
        elif j=='#':
            sum-=7
            continue
        else:
            sum+=float(j)
            continue
    print("{:.2f}".format(sum))