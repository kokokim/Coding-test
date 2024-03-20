a,b,c=map(int, input().split())

if a==b==c:
    money=10000+a*1000
elif a==b or b==c:
    money=1000+b*100
elif a==b or a==c:
    money=1000+a*100
elif a==c or c==b:
    money=1000+c*100
else:
    money=max(a,b,c)*100
    
print(money)