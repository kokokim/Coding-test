num_list=[]
for i in range(3):
    n=map(int, input().split())
    num_list.append(list(n))


for i in num_list:
    front, back=0,0

    for j in i:
        if j==0:
            front+=1
        elif j==1:
            back+=1
    if front==1:
        print("A")
    elif front==2:
        print("B")
    elif front==3:
        print("C")
    elif front==4:
        print("D")
    else:
        print("E")