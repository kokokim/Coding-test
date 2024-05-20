a,b,v=map(int, input().split())

day=(v-b)/(a-b)
if day%1==0:
    print(int(day))
else:
    print(int(day+1))