# 위상 정렬
from collections import deque

v,e = map(int,input().split())
indegree = [0]*(v+1)
# 연결 리스트 초기화 
graph =[[] for i in range(v+1)]

for _ in range(e):
  a,b = map(int,input().split())
  # a 에서 b로 이동 가능 
  graph[a].append(b)
  # 진입 차수 증가 
  indegree[b] += 1

# 위상 정렬 함수 
def topology_sort():
  result = []
  q = deque()
  
  # 처음 시작할 때 진입차수가 0 인 노드를 큐에 삽입 
  for i in range(1,v+1):
    if indegree[i]==0:
      q.append(i)

  while q:
    now = q.popleft()
    result.append(now)
    for i in graph[now]:
      indegree[i]-=1
      if indegree[i]==0:
        q.append(i)
  
  for i in result:
    print(i,end= ' ')

topology_sort()
