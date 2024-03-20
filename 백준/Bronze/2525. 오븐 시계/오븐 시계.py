h, m=map(int, input().split())
t=int(input())

i=(m+t)//60
nm=(m+t)%60

if m+t>=60:
    if h+i>23:
        h=(h+i)%24
        m=nm
    else:
        h+=i
        m=nm
else:
    m=nm

print(h, m)
    