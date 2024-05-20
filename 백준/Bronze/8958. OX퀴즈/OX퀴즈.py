n=int(input())
test_case=[]
num=0
score=0
for i in range(0, n):
    a=input()
    test_case.append(a)

for i in test_case:
    for j in i:
        if(j=='O'):
            num+=1
        elif(j=='X'):
            num=0
        score+=num
    print(score)
    score, num=0,0