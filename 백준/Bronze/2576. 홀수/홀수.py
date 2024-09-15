odd_list=[]
sum=0

for i in range(7):
    n=int(input())
    if n%2!=0:
        odd_list.append(n)
        sum+=n

if len(odd_list)==0:
    print(-1)
else:
    odd_list=sorted(odd_list)
    print(sum)
    print(odd_list[0])