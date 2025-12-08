import sys
import heapq

proclimit = 1000
#proclimit = 10

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

np = len(points)

edges = []
for i in range(np):
  dist = []
  x1, y1, z1 = points[i]
  for j in range(i+1, np):
    x2, y2, z2 = points[j]
    dx = x1 - x2
    dy = y1 - y2
    dz = z1 - z2
    d2 = dx*dx + dy*dy + dz*dz
    dist.append((d2, i, j))
  edges.extend(heapq.nsmallest(10, dist))

edges.sort()

parent = list(range(np))
size = [1] * np

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

processed = 0
for d2, a, b in edges:
  union(a, b)
  processed += 1
  if processed == proclimit:
    break

circuits = []
for i in range(np):
  if parent[i] == i:
    circuits.append(size[i])

circuits.sort(reverse=True)

answer = circuits[0] * circuits[1] * circuits[2]

print("Answer is: ", answer)
