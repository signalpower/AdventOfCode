import sys
import heapq

proclimit = 1000
#proclimit = 10
numedges = 50

if len(sys.argv) < 2:
  print("Usage python ",sys.argv[0], "<input file>")
  sys.exit(1)

try:
  with open(sys.argv[1], "r") as f:
    inputdata = f.read()
except FileNotFoundError:
  print("Error: The file was not found.")
  sys.exit(1)

points = [tuple(map(int, line.split(','))) for line in inputdata.splitlines() if line.strip()]

numpoints = len(points)

edges = []
for i in range(numpoints):
  x1, y1, z1 = points[i]
  heap = []
  for j in range(i+1, numpoints):
    x2, y2, z2 = points[j]
    dx = x1 - x2
    dy = y1 - y2
    dz = z1 - z2
    d2 = dx*dx + dy*dy + dz*dz

    if len(heap) < numedges:
      heapq.heappush(heap, (-d2, j))
    else:
      if d2 < -heap[0][0]:
        heapq.heapreplace(heap, (-d2, j))
  for neg_d2, j in heap:
    edges.append((-neg_d2, i, j))

edges.sort()

parent = list(range(numpoints))
size = [1] * numpoints

def find(x):
  if parent[x] != x:
    parent[x] = find(parent[x])
  return parent[x]

def union(a, b):
  ra = find(a)
  rb = find(b)
  if ra == rb:
    return False
  if size[ra] < size[rb]:
    parent[ra] = rb
    size[rb] += size[ra]
  else:
    parent[rb] = ra
    size[ra] += size[rb]
  return True


comps = numpoints
for d2, a, b in edges:
  if union(a, b):
    comps -= 1
    la, lb = a, b
    if comps == 1:
      break

if comps != 1:
  print("WARNING: not fully connected — increase numedges")

answer = points[la][0] * points[lb][0]

print("Answer is: ", answer)
