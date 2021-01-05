# 서로소 집합을 활용한 사이클 판별 
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

# 노드의 개수와 간선의 개수 입력 받기 
v,e = map(int,input().split())
parent = [0]*(v+1)

for i in range(1,v+1):
  parent[i]=i

# 사이클 판단 
cycle = False

# union 연산을 수행 
for i in range(e):
  a,b = map(int,input().split())
  # 사이클이 발생했다면 종료 
  if find_parent(parent,a) == find_parent(parent,b):
    cycle = True
    break
  # 사이클이 발생하지 않았다면 합집합 수행 
  else:
    union_parent(parent,a,b)

if cycle:
  print("사이클이 발생했습니다.")
else:
  print("사이클이 발생하지 않았습니다.")