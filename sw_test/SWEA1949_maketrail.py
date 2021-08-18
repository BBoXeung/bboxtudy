'''
=== SWEA 1949 ===
[입력]
2     
5 1       
9 3 2 3 2 
6 3 1 7 5
3 4 8 9 9
2 3 7 7 7
7 6 5 5 8
3 2       
1 2 1     
2 1 2
1 2 1

[출력]
#1 6
#2 3
'''
dx = [-1,1,0,0]
dy = [0,0,-1,1]

def checkBoundary(x,y):
  if 0 <= x < N and 0 <= y < N and visited[x][y] == False:
    return True
  else:
    return False

def DFS(x,y,k,l):
  global result
  if result < l:
    result = l
  for i in range(4):
    if result == MAXL:
      return
    nx = x+dx[i]
    ny = y+dy[i]
    if not checkBoundary(nx,ny): continue
    if board[x][y] > board[nx][ny]:
      visited[nx][ny] = True
      DFS(nx,ny,k,l+1)
      visited[nx][ny] = False
    else:
      if board[x][y] > board[nx][ny]-k and board[x][y] > 0:
        temp = board[nx][ny]
        board[nx][ny] = board[x][y] - 1
        visited[nx][ny] = True
        DFS(nx,ny,0,l+1)
        visited[nx][ny] = False
        if board[nx][ny] != temp:
          board[nx][ny] = temp

for t in range( int(input()) ):
  # Input
  N, K = map( int, input().split() )
  board = [ list(map(int,input().split())) for _ in range(N) ]

  # Initial Parameter
  MAXPEAK = 20
  MAXCOUNT = 5
  peak = 0 
  for i in range(N):
    for j in range(N):
      if peak < board[i][j]:
        peak = board[i][j]
      if peak == MAXPEAK: break 
    if peak == MAXPEAK: break 

  visited = [[False for _ in range(N)] for _ in range(N)]
  MAXL = peak+1
  result = 0
  for i in range(N):
    for j in range(N):
      if peak == board[i][j]:
        visited[i][j] = True
        DFS(i,j,K,1)
        visited[i][j] = False
      if result == MAXL: break
    if result == MAXL: break

  # Print Result
  print(f'#{t+1} {result}')