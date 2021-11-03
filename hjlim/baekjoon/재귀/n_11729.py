# baekjoon problem no.11729
# 첫째 줄에 첫 번째 장대에 쌓인 원판의 개수 N (1 ≤ N ≤ 20)이 주어진다.

import sys
def hanoi_tower(n, a, b) :
    if n == 1 :
        print(a, b)
        return
       
    hanoi_tower(n-1, a, 6-(a+b)) 
    print(a, b) 
    hanoi_tower(n-1, 6-(a+b), b) 

n = int(sys.stdin.readline())
print(2**n-1)
hanoi_tower(n, 1, 3)
