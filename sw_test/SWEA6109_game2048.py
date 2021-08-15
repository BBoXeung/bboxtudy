'''
=== SWEA 6109 ===

[입력]
2
5 up
4 8 2 4 0
4 4 2 0 8
8 0 2 4 4
2 2 2 2 8
0 2 2 0 0
2 down
16 2
0 2

[출력]
#1
8 8 4 8 8
8 4 4 2 4
2 4 2 0 8
0 0 0 0 0
0 0 0 0 0
#2
0 0
16 4
'''
def move(_n, _m):
  _tmp = [[0 for _ in range(_n)] for _ in range(_n)]
  for i in range(_n):
    idx = 0
    toggle = False
    for j in range(_n):
      if _m[j][i] == 0:
        continue
      if not toggle and _m[j][i] != 0:
        _tmp[idx][i] = _m[j][i]
        toggle = True
      elif toggle and _m[j][i] != 0:
        if _tmp[idx][i] == _m[j][i]:
          _tmp[idx][i] *= 2
          toggle = False
          idx += 1
        else:
          idx += 1
          _tmp[idx][i] = _m[j][i]  
  return _tmp

def rotate(_n,_m):
  _tmp = [[0 for _ in range(_n)] for _ in range(_n)]
  for i in range(_n):
    for j in range(_n):
      _tmp[j][_n-i-1] = _map[i][j]
  return _tmp

for t in range(int(input())):
  
  # Input
  n, dir = input().split()
  n = int(n)
  _map = [0 for _ in range(n)]
  for i in range(n):
    _map[i] = list(map(int,input().split()))

  # Move Up
  if dir == 'up':
    _map = move(n,_map)
  
  # Move Left
  if dir == 'left':
    _map = rotate(n,_map)
    _map = move(n,_map)
    for _ in range(3):
      _map = rotate(n,_map)

  # Move Right
  if dir == 'right':
    for _ in range(3):
      _map = rotate(n,_map)
    _map = move(n,_map)
    _map = rotate(n,_map)
  
  # Move Down
  if dir == 'down':
    for _ in range(2):
      _map = rotate(n,_map)
    _map = move(n,_map)
    for _ in range(2):
      _map = rotate(n,_map)
      
  # Print Result
  print(f'#{t+1}')
  for i in range(n):
    for j in range(n):
      print(_map[i][j],end=" ")
    print()