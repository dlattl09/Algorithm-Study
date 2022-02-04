N, M = map(int, input().split())
board = []
paint = []

for _ in range(N):
    board.append(input())

for a in range(N-7):
    for b in range(M-7):
        idx1 = 0
        idx2 = 0
        for i in range(a, a+8):
            for j in range(b, b+8):
                if (i+j) % 2 == 0:
                    if board[i][j] != 'W':
                        idx1 += 1
                    if board[i][j] != 'B':
                        idx2 += 1
                else:
                    if board[i][j] != 'B':
                        idx += 1
                    if board[i][j] != 'W':
                        idx += 1
        paint.append(min(index1, index2))

print(min(paint))
