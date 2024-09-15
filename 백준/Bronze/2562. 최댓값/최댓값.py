num_list=[]

for i in range(9):
    n=int(input())
    num_list.append(n)

num_max=max(num_list)
index=num_list.index(num_max) +1

print(num_max)
print(index)