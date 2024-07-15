n=int(input())
arr=[]
s=0
for i in range(n):
    a=int(input())
    arr.append(a)

for i in range(n):
    min_index=i
    for j in range(i+1, n):
        if arr[min_index] > arr[j]:
            min_index=j
    arr[i], arr[min_index] = arr[min_index], arr[i]

for i in arr:
    print(i)