#첫째 줄에 수의 개수 N(1 ≤ N ≤ 500,000)이 주어진다. 
#단, N은 홀수이다. 그 다음 N개의 줄에는 정수들이 주어진다.
#입력되는 정수의 절댓값은 4,000을 넘지 않는다.

import math
from collections import Counter 
import sys

n = int(sys.stdin.readline())
numbers = []
for i in range(n):
    numbers.append(int(sys.stdin.readline()))

numbers.sort()
counting = Counter(numbers).most_common()

print(int(round(sum(numbers)/n)))
print(numbers[len(numbers)//2])
if len(counting) > 1:
    if counting[0][1] == counting[1][1]:
        print(counting[1][0])
    else:
        print(counting[0][0])
else:
    print(counting[0][0])
print(numbers[-1]-numbers[0])
