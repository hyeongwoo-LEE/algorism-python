import sys

input = sys.stdin.readline
n,m = map(int,input().split())

INF = int(1e9)

graph = [[INF]*(n+1) for _ in range(n+1)]

#자기 자신으로 가는 비용 0
for a in range(1, n+1):
  for b in range(1, n+1):
    if a == b:
      graph[a][b] = 0

#간선 정보 입력받기 - 스트레이트로 갈 경우
for _ in range(m):
  a,b,c = map(int,input().split())
  graph[a][b] = c

#점화식으로 알고리즘 수행
for k in range(1,n+1):
  for a in range(1,n+1):
    for b in range(1, n+1):
      graph[a][b] = min(graph[a][b],graph[a][k]+graph[k][b])

for a in range(1, n+1):
  for b in range(1, n+1):
    if graph[a][b] == INF:
      print("INFINITY", end=" ")
    else:
      print(graph[a][b], end=" ")
  print()

