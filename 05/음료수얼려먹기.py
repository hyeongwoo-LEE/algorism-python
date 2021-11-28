n,m = map(int, input().split())

graph = []

for _ in range(n):
  graph.append(list(map(int,input().split())))

def dfs(x, y):
  if x <= -1 or y <= -1 or x >= n or y >= m:
    return False

  if graph[x][y] == 0:
    graph[x][y] = 1
    # 상하좌우 위치도 체크
    dfs(x-1,y)
    dfs(x+1,y)
    dfs(x,y-1)
    dfs(x,y+1)
    return True
  return False

result = 0
for i in range(n):
  for j in range(m):
    if dfs(i,j) == True:
      result += 1

print(result)