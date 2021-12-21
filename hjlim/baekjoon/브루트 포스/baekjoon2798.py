from itertools import combination

N, M = map(int, input().split())
cards = list(map(int, input().split()))
ans = 0

for i in combinations(cards,3):
  cand = sum(i)
  if ans < cand <= M:
    ans = cand
print(ans)
