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

rows = [line.rstrip("\n") for line in inputdata.splitlines()]
width = max(len(r) for r in rows)
matrix = [[-1 if ch == '^' else 1 if ch == "S" else 0 if ch == "." else ch for ch in r.ljust(width)] for r in rows ]
height = len(matrix)

for y in range(1, height):
  for x in range(width):
    a = matrix[y-1][x]
    if a > 0:
      if matrix[y][x] < 0:
        matrix[y][x-1] += a
        matrix[y][x+1] += a
      else:
        matrix[y][x] += a

print("Answer is: ", sum(matrix[-1]))
