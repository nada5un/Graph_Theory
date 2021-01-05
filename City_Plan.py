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

# 집의 개수 n , 길의 개수 m 
n, m = map(int,input().split())
parent = [0] * (n+1)

edges = []
result = 0

for i in range(1,n+1):
  parent[i]=i

for _ in range(m):
  # a 번과 b 번 집 연결하는 유지비 c 
  a,b,c = map(int,input().split())
  edges.append((c,a,b))

edges.sort()
last = 0

for edge in edges:
  c,a,b = edge
  # 사이클이 발생하지 않는 경우에만 
  if find_parent(parent,a) != find_parent(parent,b):
    union_parent(parent,a,b)
    result += c
    last = c

print(result-last)

