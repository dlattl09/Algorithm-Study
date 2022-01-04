num = int(input())
size = []

for i in range(num):
  size.append(input().split())
  
for i in range(num):
    rank = 1
    for j in range(num):
        if size[i][0] < size[j][0] and size[i][1] < size[j][1]:
            rank = rank + 1
    print(rank,end=" ")
  
