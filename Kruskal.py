# 크루스칼 알고리즘 

def find_parent(parent,x):
  # 루트 노드가 아니라면, 루트 노드를 찾을 때 까지 호출 
  # 경로 압축 적용  
  if parent[x] != x:
    parent[x] = find_parent(parent,parent[x])
  return parent[x]

# 부모 합치기 
def union_parent(parent,a,b):
  a = find_parent(parent,a)
  b = find_parent(parent,b)
  if a<b:
    parent[b] = a
  else:
    parent[a] = b

# 노드, 간선 개수 입력 받기 
v,e = map(int,input().split())
parent = [0]*(v+1)

# 간선 리스트, 최종 비용 
edges = []
result = 0

for i in range(1,v+1):
  parent[i] = i

for i in range(e):
  a, b, cost = map(int,input().split())
  edges.append((cost,a,b))

edges.sort()

for edge in edges:
  cost, a, b = edge
  # 사이클이 발생하지 않는 경우에만 집합에 포함 
  if find_parent(parent,a) != find_parent(parent,b):
    union_parent(parent,a,b)
    result += cost 

print(result)
  