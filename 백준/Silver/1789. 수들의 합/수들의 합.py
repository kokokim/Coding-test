S=int(input())
sum, i=0,0

while sum<=S:
    i+=1
    sum+=i
    
if sum==S:
    print(i)
else:
    print(i-1)