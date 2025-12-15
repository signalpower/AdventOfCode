import sys

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
  x1, y1 = points[i]
  x2, y2 = points[(i+1) % np]
  edges.append((x1, y1, x2, y2))

vertical_edges = []
for i in range(np):
  x1, y1 = points[i]
  x2, y2 = points[(i+1) % np]
  if x1 == x2:
    ymin = min(y1, y2)
    ymax = max(y1, y2)
    vertical_edges.append((x1, ymin, ymax))

Ylevels = sorted(set(y for (_,y) in points))

Ytest = []
for a, b in zip(Ylevels, Ylevels[1:]):
  Ytest.append(a)
  Ytest.append((a + b) // 2)
Ytest.append(Ylevels[-1])


def inside(px, py):
  for (x, y1, y2) in vertical_edges:
    if px == x and y1 <= py <= y2:
      return True

  for (x1,y1,x2,y2) in edges:
    if y1 == y2 and y1 == py and min(x1,x2) <= px <= max(x1,x2):
      return True

  count = 0
  for (x, y1, y2) in vertical_edges:
    if y1 <= py < y2 and px < x:
      count += 1

  return (count % 2) == 1


def rect_inside(xmin, xmax, ymin, ymax):
  xl = xmin + 1
  xr = xmax - 1
  if xl > xr:
    return False
  for y in Ytest:
    if y < ymin or y > ymax:
      continue
    if not inside(xl, y):
      return False
    if not inside(xr, y):
      return False
  return True


maxarea = 0
pointA = None
pointB = None
for i in range(np):
  x1, y1 = points[i]
  for j in range(i+1, np):
    x2, y2 = points[j]
    if x1 == x2 or y1 == y2:
      continue
    xmin, xmax = sorted([x1, x2])
    ymin, ymax = sorted([y1, y2])
    area = (xmax - xmin + 1) * (ymax - ymin + 1)
    if area <= maxarea:
      continue
    if rect_inside(xmin, xmax, ymin, ymax):
      maxarea = area
      pointA = points[i]
      pointB = points[j]

print("Answer is: ", maxarea, "for pointA:", pointA, "and pointB:", pointB)

