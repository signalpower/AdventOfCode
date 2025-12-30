import sys

if len(sys.argv) < 2:
  print("Usage: python ",sys.argv[0], "<input file>")
  sys.exit(1)

try:
  with open(sys.argv[1], "r") as f:
    inputdata = f.read()
except FileNotFoundError:
  print("Error: The file was not found.")
  sys.exit(1)

result = 0

shapes = {}
shape_idx = None
for line in inputdata.splitlines():
  if line.strip().endswith(":"):
    shape_idx = int(line[:-1])
    shapes[shape_idx] = 0
  elif "#" in line:
    shapes[shape_idx] += line.count("#")
  elif "x" in line:
    dim, raw_counts = line.split(":")
    w, h = map(int, dim.split("x"))
    counts = map(int, raw_counts.split())
    shape_count = sum(shapes.get(idx, 0) * count for idx, count in enumerate(counts))
    if shape_count <= w * h:
      result += 1

print("Answer is: ", result)
