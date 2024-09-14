T=int(input())
A=[]
B=[]

for i in range(0,T):
    a,b=map(int, input().split())
    A.append(a)
    B.append(b)

for i in range(0, T):
    print(f"Case #{i+1}: {A[i]} + {B[i]} = {A[i]+B[i]}")