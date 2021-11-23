
'''
유니온 파인드 알고리즘
1. find : 노드 x가 어느 집합에 포함되어 있는지 찾는 연산
2. union : 노드 x가 포함된 집합과 노드 y가 포함된 집합을 합치는 연산.
'''
import sys
input = sys.stdin.readline

G = int(input())
P = int(input())

plane_lst = []
for _ in range(P):
  plane_lst.append(int(input()))

gate = [x for x in range(G+1)]

def find(p):
  if p == gate[p]:
    return p
  parent = find(gate[p])
  gate[p] = parent
  return parent

def union(p):
  gate[find(p)] = find(p-1)

total = 0
for plane in plane_lst:
  parent = find(plane)
  if parent == 0:
    break
  total += 1
  union(parent)

print(total)