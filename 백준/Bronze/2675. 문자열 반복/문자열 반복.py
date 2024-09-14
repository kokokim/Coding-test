T=int(input())
iterator=[]
s_list=[]

for i in range(T):
    R, S=map(str, input().split())
    R=int(R)
    iterator.append(R)
    s_list.append(list(S))
n=0
for i in s_list:
    for j in i:
        num=iterator[n]
        print(j*num, end="")
    print()
    n+=1