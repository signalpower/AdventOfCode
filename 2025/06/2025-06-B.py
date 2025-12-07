import sys
from math import prod

if len(sys.argv) < 2:
  print("Usage python ",sys.argv[0], "<input file>")
  sys.exit(1)

with open(sys.argv[1], "r") as f:
  inputdata = f.read()

tot = start = end = 0
rows = [line.rstrip("\n") for line in inputdata.splitlines()]
width = max(len(r) for r in rows)
matrix = [list(r.ljust(width)) for r in rows]
empty_cols = [all(ch == " " for ch in col) for col in zip(*matrix)]
empty_cols.append(True)
for col in range(width+1):
  if empty_cols[col]:
    if end > start:
      col_block = [row[start:end] for row in matrix]
      num_rot = list(map(list, zip(*col_block[:-1])))[::-1]
      num_int = [int(d) for d in ("".join(c for c in r if c.isdigit()) for r in num_rot) if d]
      subtot = prod(num_int) if "*" in col_block[-1] else sum(num_int)
      tot += subtot
      start = end
  end += 1

print("Answer is: ", tot)

