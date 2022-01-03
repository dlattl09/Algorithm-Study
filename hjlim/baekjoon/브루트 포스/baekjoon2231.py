import sys

N = int(sys.stdin.readline())
for i in range(1,N):
  M = sum(map(int, str(i))) + N
  if M==N:
    print(M)
    break
  
