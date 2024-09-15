sum=0
num_list=[]

for i in range(5):
    n=int(input())
    num_list.append(n)
    sum+=n

num_list=sorted(num_list)

print(sum//5)
print(num_list[2])