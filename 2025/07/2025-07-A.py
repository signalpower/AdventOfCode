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
matrix = [list(r.ljust(width)) for r in rows]
height = len(matrix)

for c in range(width):
  if matrix[0][c] == "S":
    matrix[1][c] = "s"

splits = 0
for y in range(2, height):
  for x in range(width):
    if matrix[y-1][x] == "s":
      if matrix[y][x] == "^":
        matrix[y][x-1] = "s"
        matrix[y][x+1] = "s"
        splits += 1
      elif matrix[y][x] == ".":
        matrix[y][x] = "s"

print("Answer is: ", splits)
