from itertools import combinations

# 특정 원소가 속한 집합을 찾기
def find(parent, x):
    if parent[x] == x:
        return x
    parent[x] = find(parent, parent[x])
    return parent[x]


# 두 원소가 속한 집합을 합치기 (간선 연결한다고 생각!)
def union(parent, a, b):
    rootA = find(parent, a)
    rootB = find(parent, b)

    if rootA < rootB:
        parent[rootB] = rootA
    else:
        parent[rootA] = rootB


import sys

input = sys.stdin.readline
# 노드의 개수와 간선(union 연산)의 개수 입력받기
n = int(input())
position = []
for _ in range(n):
    x, y, z = map(int, input().split())
    position.append((x,y,z))

parent = [0] * n
# 부모 테이블상에서, 부모를 자기 자신으로 초기화
for i in range(n):
    parent[i] = i

lines = list(combinations(parent,2))

edges = []

# 모든 간선에 대한 정보를 입력받기
for line in lines:
    a, b = line
    cost = min(abs(position[a][0] - position[b][0]),
    abs(position[a][1] - position[b][1]),
    abs(position[a][2] - position[b][2]))

    # 비용순으로 오름차순 정렬하기 위해 튜플의 첫 번째 원소를 비용으로 설정
    edges.append((cost, a, b))

result = 0
edges.sort()

for edge in edges:
    cost, a, b = edge
    # 사이클이 발생하지 않는 경우에만 집합에 포함(=연결한다.)
    if find(parent, a) != find(parent, b):
        union(parent, a, b)
        result += cost

print(result)