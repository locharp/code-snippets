def check(p, q, r):
  if p == q and q == r:
    print('Player', 1 if p == 'X' else 2)
    quit()
board = (input().split(), input().split(), input().split())
for i in range(3):
  check(*board[i])
  check(board[0][i], board[1][i], board[2][i])
check(board[0][0], board[1][1], board[2][2])
check(board[0][2], board[1][1], board[2][0])
print('Draw')