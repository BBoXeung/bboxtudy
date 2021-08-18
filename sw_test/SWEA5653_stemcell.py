'''
=== SWEA 5653 ===

[입력]
ALL INPUT : SWEA5653_input.txt
PARTIAL INPUT :
3
2 2 10
1 1
0 2
5 5 19
3 2 0 3 0
0 3 0 0 0
0 0 0 0 0
0 0 1 0 0
0 0 0 0 2
9 10 37                
0 0 0 0 0 0 0 0 3 0
0 0 0 0 0 0 0 0 5 3
0 0 2 0 0 0 0 4 0 0
3 0 0 0 0 0 4 0 0 0
0 0 0 0 0 3 5 0 0 2
0 0 0 0 0 0 0 0 0 5
0 0 0 0 0 0 0 0 2 3
0 0 0 0 0 0 0 0 0 0
0 0 2 2 0 0 0 0 0 0

[출력]
#1 22
#2 36
#3 90
'''
MAXK = 300 # 상수
dx = [0,0,-1,1]
dy = [-1,1,0,0]

def check(x,y):
  if board[x][y] == 0:
    return True
  else:
    return False

def solve(x, y):
  flag[x][y] += 1
  t = flag[x][y]
  k = board[x][y]
  if t <= k:
    # print("inactive")
    return
  else: # elif k < t <= 2*k:
    # print("active")
    if t-1 == k:
      for i in range(4):
        nx = x+dx[i]
        ny = y+dy[i]
        if check(nx,ny):
          board[nx][ny] = k
          temp.append((nx,ny))
  if t == 2*k: # print("dead cell")
    board[x][y] = -1

for t in range( int(input()) ):
  # Input & Initial parameter
  N, M, K = map( int, input().split() )
  board = [[0 for _ in range(2*MAXK+M)] for _ in range(2*MAXK+N)]
  flag = [[0 for _ in range(2*MAXK+M)] for _ in range(2*MAXK+N)]
  sub = [0 for _ in range(N)]
  order = {}
  for i in range(N):
    sub[i] = list( map(int, input().split()) )
    for j in range(M):
      board[i+MAXK][j+MAXK] = sub[i][j]
      if sub[i][j] != 0:
        order[(i+MAXK,j+MAXK)] = sub[i][j]

  # 탐색할 좌표 순서 (생존시간 큰 좌표부터 탐색)
  order = sorted(order, key = lambda x : order[x])
  
  # 탐색
  for _ in range(K): 
    temp = []
    while order:
      popx, popy = order.pop()
      solve(popx,popy)
      if board[popx][popy] != -1:
        temp.append((popx,popy))
    order = list(reversed(temp))

  # Count Result
  result = 0
  for i in range(2*MAXK+N):
    for j in range(2*MAXK+M):
      if board[i][j] > 0:
        result += 1
      #   print(board[i][j],end=" ")
      # if board[i][j] == -1:
      #   print("-1",end=" ")

  # Print Result
  print(f'#{t+1} {result}')
  