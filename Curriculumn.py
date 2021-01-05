from collections import deque
import copy

n = int(input())
indegree = [0]*(n+1)
graph = [[] for i in range(n+1)]
hour = [0]*(n+1)

for i in range(1,n+1):
  a = list(map(int,input().split()))
  hour[i] = a[0]
  # a 리스트에서 범위 지정 
  for x in a[1:-1]:
    indegree[i]+=1
    graph[x].append(i)
    
# 위상 정렬 함수 
def topology_sort():
  result = copy.deepcopy(hour)
  q = deque()
  
  # 처음 시작할 때 진입차수가 0 인 노드를 큐에 삽입 
  for i in range(1,n+1):
    if indegree[i]==0:
      q.append(i)

  while q:
    now = q.popleft()
    for i in graph[now]:
      result[i] = max(result[i],result[now]+hour[i])
      indegree[i]-=1
      if indegree[i]==0:
        q.append(i)
  
  for i in range(1,n+1):
    print(result[i])

topology_sort()