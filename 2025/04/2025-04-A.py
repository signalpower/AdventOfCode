import sys

if len(sys.argv) < 2:
  print("Usage python ",sys.argv[0], "<input file>")
  sys.exit(1)

try:
  with open(sys.argv[1], "r") as infile:
    grid = [line.strip() for line in infile if line.strip()]
except FileNotFoundError:
  print("Error: The file was not found.")
  sys.exit(1)

CC = '@'
GH = len(grid)
GW = len(grid[0])  # if GH > 0 else 0

ofs = [
    (-1, -1), ( 0, -1), ( 1, -1),
    (-1,  0),           ( 1,  0),
    (-1,  1), ( 0, 1),  ( 1,  1)
]

p = 0

for y in range(len(grid)):
  for x in range(len(grid[y])):
    if grid[y][x] == CC:
      nc = 0
      for dx, dy in ofs:
        nx = x + dx
        ny = y + dy
        if (0 <= nx < GW) and (0 <= ny < GH):
          if grid[ny][nx] == CC:
            nc += 1
      if nc < 4:
        p += 1

print("Answer is: ", p)
