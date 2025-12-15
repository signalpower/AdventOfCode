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

maxarea = 0
for i in range(np):
  x1, y1 = points[i]
  for j in range(i+1, np):
    x2, y2 = points[j]
    area = (abs(x1 - x2) + 1) * (abs(y1 - y2) + 1)
    if area > maxarea:
      maxarea = area

print("Answer is: ", maxarea)
