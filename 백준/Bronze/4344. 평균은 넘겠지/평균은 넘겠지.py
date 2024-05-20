c=int(input())
test_case=[]
for i in range(0, c):
    test_case.append(list(map(int, input().split())))

num=0
for i in test_case:
    for j in i[1:]:
        m=sum(i[1:])/i[0]
        if j>m:
            num+=1
    p=num/i[0]*100
    print("{:.3f}".format(p), "%")
    num=0