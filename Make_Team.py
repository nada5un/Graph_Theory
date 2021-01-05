# 특정 원소가 속한 집합 찾기 
def find_parent(parent,x):
  if parent[x] != x:
    parent[x] = find_parent(parent,parent[x])
  return parent[x]

# 두 원소가 속한 집합을 합치기 
def union_parent(parent,a,b):
  a = find_parent(parent,a)
  b = find_parent(parent,b)
  if a<b:
    parent[b] = a
  else:
    parent[a] = b

# n개의 팀, m개의 연산 
n,m = map(int,input().split())
parent = [0]*(n+1)

for i in range(1,n+1):
  parent[i]=i

for _ in range(m):
  check,a,b = map(int,input().split())
  # 합치기 연산 
  if check == 0:
    union_parent(parent,a,b)
  # 같은 팀 여부 확인 
  elif check == 1:
    if find_parent(parent,a) == find_parent(parent,b):
      print("YES")
    else:
      print("NO")

