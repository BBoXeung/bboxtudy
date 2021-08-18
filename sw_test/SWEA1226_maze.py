'''
=== SWEA 1226 ===
[입력]
1
1111111111111111
1210000000100011
1010101110101111
1000100010100011
1111111010101011
1000000010101011
1011111110111011
1010000010001011
1010101111101011
1010100010001011
1010111010111011
1010001000100011
1011101111101011
1000100000001311
1111111111111111
1111111111111111
2
1111111111111111
1200000010000011
1011111011111011
1000001010000011
1110101010111011
1010101010100011
1011111010111111
1000001010000011
1011101011111011
1010101010000011
1010101010111111
1010100000130011
1010111111111011
1000000000000011
1111111111111111
1111111111111111

[출력]
#1 1
#2 1
'''

# T = 10 # Test Case 개수
T = 2 # Sample
dx = [-1,1,0,0]
dy = [0,0,-1,1]

def checkBoundary(x,y):
  if 0 <= x < N and 0 <= y < N and board[x][y] != 1 and visited[x][y] == False:
    return True
  else:
    return False

def DFS(x,y,tx,ty):
  global result
  if x == tx and y == ty:
    result = 1
    return
  for i in range(4):
    nx = x+dx[i]
    ny = y+dy[i]
    if not checkBoundary(nx,ny): continue
    visited[nx][ny] = True
    DFS(nx,ny,tx,ty)
    visited[nx][ny] = False

for _ in range(T):
  # Input & Initialize
  N = 16
  result = 0
  t = int(input())
  board = [list( map(int,input()) ) for _ in range(N)]
  visited = [[False for _ in range(N)] for _ in range(N)]

  # 시작점, 도착점 좌표확인
  sx,sy,ex,ey = 0,0,0,0
  for i in range(N):
    for j in range(N):
      if board[i][j] == 2:
        sx, sy = i, j
      if board[i][j] == 3:
        ex, ey = i, j

  # 탐색
  visited[sx][sy] = True
  DFS(sx,sy,ex,ey)

  # Print Result
  print(f'#{t} {result}')