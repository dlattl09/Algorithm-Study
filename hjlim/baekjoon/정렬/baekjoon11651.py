# 첫째 줄에 점의 개수 N (1 ≤ N ≤ 100,000)이 주어진다.
# 둘째 줄부터 N개의 줄에는 i번점의 위치 xi와 yi가 주어진다.
# (-100,000 ≤ xi, yi ≤ 100,000) 좌표는 항상 정수이고, 위치가 같은 두 점은 없다.

n = int(input())
coord = []
for i in range(n):
    coord.append(list(map(int, input().split())))
    
coord.sort(key=lambda x:(x[-1],x[0]))

for i in coord:
    print(i[0], i[1])
